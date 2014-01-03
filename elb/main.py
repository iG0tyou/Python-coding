__author__ = 'sunny'

import os
import json
import time

def _popen(cmd):
    print('start exec cmd:' + cmd)
    f = os.popen(cmd)
    content = f.read()
    exit_status = f.close()
    return content

script = 'python /home/sunny/PycharmProjects/elb/tengine_netlfow.py'
context = ''
ports = ' 11180   9090'


#python script_name context args

def test_tegine_netflow():
    script = 'python /home/sunny/PycharmProjects/elb/tengine_netlfow.py'
    exec_cmd(script)


def test_tegine_status():
    script = 'python /home/sunny/PycharmProjects/elb/tengine_status.py'
    exec_cmd(script)


def exec_cmd(script):
    global context
    content = _popen(script + " '" + context + "'" + " '" + ports + "'" )
    map = json.loads(content)
    if map.has_key('context'):
        context = map['context']
        print 'context:'
        print json.loads(context)
        print 'result:'
        print json.loads(map['rusult'])
        # print json.loads(map['rusult'])['total']
        print ''




while True:
    # test_tegine_status()

    test_tegine_netflow()
    time.sleep(5)

