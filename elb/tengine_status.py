#coding:utf-8
__author__ = 'linzhixian@corp.netease.com'

import urllib2
import time
import sys
import json

def time_in_millisecond():
    """
    获取当前时间
    """
    return int(time.time() * 1000)


def get_nginx_status(url):
    """
    访问获取Nginx统计信息到url，解析数据，返回dict

    访问url获取到统计信息：
    Active connections: 2
    server accepts handled requests request_time
    3 3 7 0
    Reading: 1 Writing: 1 Waiting: 0

    """
    request = urllib2.Request(url)
    res_data = urllib2.urlopen(request)
    lines = res_data.readlines()

    length = len(lines)
    if length == 4:
        for i in range(0, length):
            lines[i] = lines[i].strip()

        strs = lines[0].split()
        # print strs
        active_connections = strs[2]

        strs = lines[2].split()
        accepts = int(strs[0])
        handled = int(strs[1])
        requests = int(strs[2])
        request_time = int(strs[3])
        # print strs
        strs = lines[3].split()
        reading = int(strs[1])
        writing = int(strs[3])
        waiting = int(strs[5])
        # print strs

        status = dict()
        status['active_connections'] = active_connections
        status['accepts'] = accepts
        status['handled'] = handled
        status['requests'] = requests
        status['request_time'] = request_time
        status['reading'] = reading
        status['writing'] = writing
        status['waiting'] = waiting
        status['execTime'] = time_in_millisecond()
        return status

def get_inc_nginx_status(current_status, old_status):
    """
    根据当前到状态数据跟上一次到状态数据，计算增量
    """
    status = dict(current_status)
    keys = ['accepts', 'requests', 'handled', 'request_time']
    for key in keys:
        status[key] = current_status[key] - old_status[key]
        if status[key] < 0:
            status[key] = 0
    return status



def print_script_result(result_dict, context_dict):
    map = dict()
    map['rusult'] = json.dumps(result_dict)
    map['context'] = json.dumps(context_dict)
    print json.dumps(map),
    sys.stdout.flush()




def parse_script_context(default_dict):
    argc = len(sys.argv)
    if argc > 1:
        value = sys.argv[1]
        if value:
            script_context_ditc = json.loads(value)
            return script_context_ditc
    return default_dict






def main():
    url = 'http://localhost/nginx-status'
    current_status = get_nginx_status(url)
    # print current_status

    old_status = parse_script_context(current_status)

    inc_status = get_inc_nginx_status(current_status, old_status)
    # print inc_status

    print_script_result(inc_status, current_status)


if __name__ == '__main__':
    main()

