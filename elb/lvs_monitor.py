#!/usr/bin/python
#_*_ coding:UTF-8 _*_
__author__ = 'sunlzx'

import os
import string
import json
import exceptions

def _atoi(value):
    if isinstance(value, (int, long, float)):
            return value

    rate = 1
    if value.endswith('K') or value.endswith('k'):
        rate = 1024
    elif value.endswith('M') or value.endswith('m'):
        rate = 1024 * 1024
    elif value.endswith('G') or value.endswith('g'):
        rate = 1024 * 1024 * 1024

    if (rate == 1):
        return string.atoi(value)
    else:
        return string.atoi(value[:-1]) * rate
    pass

def exec_cmd(cmd):
    file = os.popen(cmd)
    lines = file.readlines()
    exit_status = file.close()
    if exit_status == None or exit_status == 0:
        return lines
    else:
        raise exceptions.RuntimeError('exec cmd fial:' + cmd + ", exit status:" + str(exit_status))



class ServerStats:
    """
    LVS Server Stats
    sudo ipvsadm -L -n --stats
    """

    def __init__(self, stats=None):
            self.address = stats[1]
            self.conns = _atoi(stats[2])
            self.inPkts = _atoi(stats[3])
            self.outPkts = _atoi(stats[4])
            self.inBytes = _atoi(stats[5])
            self.outBytes = _atoi(stats[6])

    def __inc(self, current_stats_dict, last_stats_dict, key):
        return  current_stats_dict[key] - last_stats_dict[key]

    def get_server_stats_dict(self, current_stats_dict, last_stats_dict):
        inc_dict = dict()
        inc_dict['address'] = current_stats_dict['address']
        for key in ['conns', 'inPkts', 'outPkts', 'inBytes', 'outBytes']:
            inc_dict[key] = self.__inc(current_stats_dict, last_stats_dict, key)
        return inc_dict

    pass


class VirtualService:
    def __init__(self, protocol, address, scheduler):
        self.protocol = protocol #TCP, UDP
        self.address = address   #ip:port
        self.scheduler = scheduler #one of rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq
        self.all_real_server_dict = {}

    def add_real_server(self, realServer):
        self.all_real_server_dict[realServer.address] = realServer.__dict__;


class RealServer:
    # Forward Weight ActiveConn InActConn
    # ActiveConn - in ESTABLISHED state
    # InActConn - any other state
    def __init__(self, address, weight, activeConn, inActConn):
        self.address = address
        self.weight = _atoi(weight)
        self.activeConn = _atoi(activeConn)
        self.inActConn = _atoi(inActConn)


def get_lvs_stats(dev_mode, datas):
    if dev_mode:
        lines = open('lsv-stats', 'r').readlines()
    else:
        lines = exec_cmd('sudo ipvsadm -L -n --stats')

    current_stats_dict = {}
    for idx in range(3, len(lines), 1):
        line = lines[idx].strip()
        strs = line.split()
        if len(strs) == 7:
            stats = ServerStats(strs)
            address = stats.address
            new_stats_dict = stats.__dict__
            old_stats_dict = datas.get(address)

            if old_stats_dict:
                inc_stats_dict = stats.get_server_stats_dict(new_stats_dict, old_stats_dict)
            else:
                inc_stats_dict = stats.get_server_stats_dict(new_stats_dict, new_stats_dict)

            current_stats_dict[address] = inc_stats_dict
            datas[stats.address] = new_stats_dict;

    for key in datas.keys():
        if not current_stats_dict.has_key(key):
            print "delete:" + key
            del datas[key]
    return current_stats_dict


def get_virtual_service_dict(dev_mode = False):
    if dev_mode:
        lines = open('servers', 'r').readlines()
    else:
        lines = exec_cmd('sudo ipvsadm -L -n')

    virtual_service_dict = {}
    virtual_service = None;
    for idx in range(3, len(lines), 1):
        line = lines[idx].strip()
        strs = line.split()

        length = len(strs)
        if length == 3:
            virtual_service  = VirtualService(strs[0], strs[1], [2])
            virtual_service_dict[virtual_service.address] = virtual_service.__dict__;
        elif length == 6:
            real_server = RealServer(strs[1], strs[3], strs[4], strs[5])
            virtual_service.add_real_server(real_server)
        else:
            print 'error data:' + line
    return virtual_service_dict


def read_file_content(fileName):
    with open(fileName, 'r') as file:
        content = file.read()
    return content


def write_file_content(fileName, content):
    with open(fileName, 'w') as file:
        file.write(content)
        file.flush()


def show(virtual_service_dict, current_stats_dict):
    print "virtual_service_dict:"
    for key in virtual_service_dict:
        vs = virtual_service_dict[key]
        print key
        for rs in vs['all_real_server_dict']:
            print "    " + str(vs['all_real_server_dict'][rs])

    print "current_stats_dict:"
    for key in current_stats_dict:
        print "    " + key + ":" + str(current_stats_dict[key])


def get_lvs_all_server_stats_dict(dev_mode = False):
    global_stats_dict = {}
    filename = 'lvsNetfowStats.json'
    if os.path.isfile(filename):
        bytes = read_file_content(filename)
        if len(bytes) > 0:
            global_stats_dict = json.loads(bytes)
    # invoke
    current_stats_dict = get_lvs_stats(dev_mode, global_stats_dict)
    # write to file
    write_file_content(filename, str(json.dumps(global_stats_dict)))
    return current_stats_dict


def main():
    dev_mode = True

    virtual_service_dict = get_virtual_service_dict(dev_mode)
    lvs_all_server_stats_dict = get_lvs_all_server_stats_dict(dev_mode)
    # show
    show(virtual_service_dict, lvs_all_server_stats_dict)



if __name__ == '__main__':
    main()


