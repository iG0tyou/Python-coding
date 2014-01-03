#!/usr/bin/python
__author__ = 'sunlzx'

import time

def main():
    file = open('del_log.log','r')
    done = 0
    while not  done:
            aLine = file.readline()
            if(aLine):
                print aLine,
            else:
                print ""
                time.sleep(5)
    file.close()





if __name__ == '__main__':
    main()
