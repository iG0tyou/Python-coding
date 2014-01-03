__author__ = 'sunny'

import urllib2
import json


def get_upstream_status(uri='/rs-status', port=80):
    url = 'http://localhost:' + str(port) + uri +'?format=json'
    request = urllib2.Request(url)
    res = urllib2.urlopen(request)
    data = res.read()
    return data

def main():
    content = get_upstream_status()
    raw_servers_dict = json.loads(content)

    servers_dict = dict()
    servers_dict['server_list'] = raw_servers_dict['servers']['server']
    print json.dumps(servers_dict)


if __name__ == '__main__':
    main()

