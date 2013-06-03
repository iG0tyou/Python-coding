#coding=gbk
'''
Created on 2013-3-9

@author: sunlzx
'''

import os
import traceback
import logging

if __name__ == '__main__':
    pass

# 创建一个logger  
logger = logging.getLogger('mylogger')  
logger.setLevel(logging.DEBUG)  
  
# 创建一个handler，用于写入日志文件  
fh = logging.FileHandler('test.log')  
fh.setLevel(logging.DEBUG)  
  
# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
  
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
# 给logger添加handler  
logger.addHandler(fh)  
logger.addHandler(ch)  

logging.debug('this is a message')  
logging.debug('this is a message')  
logging.debug('this is a message')  

#print os.getcwd();
#path = os.getcwd()
#print os.path.isdir(path)
#print os.path.isfile(path)
#print os.path.islink(path)



#try:
#    f = open("R:/tm.txt", 'r');
#    print f.read()
#    print f
#    f.close()
#    im=xx
#except Exception, e: #捕获所有异常，Exception
#    print e
#    print "================="
##    traceback.print_exc()
#finally:
#    print "finally..."


