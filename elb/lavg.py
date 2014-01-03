__author__ = 'sunlzx'

import json
import sys

# 0.42 0.29 0.15 3/510 11426
def main():
     with open('/proc/loadavg', 'r') as file:
        content = file.read()
     list = content.split(' ')
     status = {}
     status['lav1'] = list[0]
     status['lav5'] = list[1]
     status['lav15'] = list[2]
     print json.dumps(status)
     sys.stdout.flush()

if __name__ == '__main__':
    main()