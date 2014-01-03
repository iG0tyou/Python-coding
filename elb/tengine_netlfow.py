__author__ = 'linzhixian@corp.netease.com'


import os
import sys
import json

def _system(cmd):
    # print('start exec cmd:' + cmd)
    ret = os.system(cmd)
    pass


def _popen(cmd):
    # print('start exec cmd:' + cmd)
    f = os.popen(cmd)
    lines = f.readlines()
    exit_status = f.close()
    return lines


def add_rule(port):
    cmd_input = 'sudo iptables -C INPUT -p tcp --dport $port || sudo iptables -A INPUT -p tcp --dport $port'
    cmd_output = 'sudo iptables -C OUTPUT -p tcp --sport $port || sudo iptables -A OUTPUT -p tcp --sport $port'
    cmd_input = cmd_input.replace('$port', str(port))
    cmd_output = cmd_output.replace('$port', str(port))
    _system(cmd_input)
    _system(cmd_output)
    pass

def delete_rule(port):
    cmd = 'sudo iptables -D INPUT -p tcp --dport $port && sudo iptables -D  OUTPUT -p tcp --sport $port'
    cmd = cmd.replace('$port', str(port))
    _system(cmd)
    pass



def get_netflow_status():
    lines = _popen("sudo iptables  -nvx -L|grep 'tcp '|awk '{print $10, $2}'")
    status = dict()
    ports = dict()
    for line in lines:
        line = line.strip()
        strs = line.split(' ')
        if len(strs) == 2:
            status[strs[0]] = int(strs[1])
            port = strs[0].split(':')[1]
            ports[port] = None
    return (status, ports)


def get_result(status, old_status, ports):
    total_input_bytes = 0
    total_output_bytes = 0
    detail_list = []
    for port in ports.keys():
        input_bytes = 0
        output_bytes = 0
        key = 'dpt:' + port
        if old_status.has_key(key):
            input_bytes = status[key] - old_status[key]
        key = 'spt:' + port
        if old_status.has_key(key):
            output_bytes = status[key] - old_status[key]
        if input_bytes < 0:
            input_bytes = 0
        if output_bytes < 0:
            output_bytes = 0
        single_status = dict()
        single_status['port'] = int(port)
        single_status['input_bytes'] = input_bytes
        single_status['output_bytes'] = output_bytes
        detail_list.append(single_status)
        total_input_bytes += input_bytes
        total_output_bytes += output_bytes
    total_status = dict()
    total_status['input_bytes'] = total_input_bytes
    total_status['output_bytes'] = total_input_bytes
    result = dict()
    result['total'] = total_status
    result['detail_list'] = detail_list
    return result


def nupdate_ports(new_ports, old_ports):
    if len(new_ports) == 0 or len(old_ports) == 0:
        return

    for port in new_ports:
        if not port in old_ports:
            print "add " + port
            add_rule(port)

    for port in old_ports:
        if not port in new_ports:
            # print "delete " + port
            delete_rule(port)







def main():
    argc = len(sys.argv)
    new_ports = []
    old_status = dict()
    for i in range(0, argc):
        value = sys.argv[i]
        value = value.strip()
        if (i == 1):
            if value:
                old_status = json.loads(value)
        if (i == 2):
            if value:
                new_ports = value.split()

    status, ports = get_netflow_status()
    nupdate_ports(new_ports, ports.keys())
    result = get_result(status, old_status, ports)

    map = dict()
    map['rusult'] = json.dumps(result)
    map['context'] = json.dumps(status)
    # print sys.argv[0] + " '" + map['context'] + "'"
    print json.dumps(map),
    sys.stdout.flush()


if __name__ == '__main__':
    main()