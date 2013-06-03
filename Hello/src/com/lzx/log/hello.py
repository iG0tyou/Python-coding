# -*- coding:utf-8 -*-
'''
Created on 2013-3-9

@author: sunlzx
'''
import sys
import locale

if __name__ == '__main__':
    pass


#如果不换行，需要添加","号
print("line"), ;
print("newline");

print "line", "newline";

print;
print "========="
'''
格式化输出
'''
count = 10;
name = "总问"


print locale.getdefaultlocale()
print sys.getdefaultencoding()

print "======encode decode=====";
a = u'中' 
b = '中'
print repr(a)
print repr(a.encode("utf-8"))
print repr(a.decode("utf-8"))
print repr(b)
print a;
print a.encode("GB18030")
print a.encode("utf-8")

f = open("aaa.txt", "w")  
f.write(a.encode("GB18030"))  

f.close() 





print isinstance(a, unicode)


print '文件系统的编码：sys.getfilesystemencoding():', sys.getfilesystemencoding() 
print '终端的输入编码：sys.stdin.encoding:', sys.stdin.encoding 
print '终端的输出编码：sys.stdout.encoding:', sys.stdout.encoding 
