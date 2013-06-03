#coding=gbk
'''
Created on 2013-3-9

@author: sunlzx
'''

import urllib

if __name__ == '__main__':
    pass

f = urllib.urlopen("http://www.baidu.com")
lines = f.readlines()
print lines
print f.info()
print f.url
for line in lines:
    print line
    print line.decode("utf-8")
    
f.close()
