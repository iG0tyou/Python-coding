#coding=utf-8
'''
Created on 2013-3-9

@author: sunlzx
'''
import urllib2
import urllib

if __name__ == '__main__':
    pass

#url = 'http://www.iteye.com';
url = "http://www.baidu.com/"
#opener = urllib2.urlopen(url)
#lines = opener.readlines()



i = 0;
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
while True:
    i = i + 1
   
    res = opener.open(url)
    print i;
    print res.readlines();






#for line in lines:
#    print line,;
 
    
opener.close()

