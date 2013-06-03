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

# ����һ��logger  
logger = logging.getLogger('mylogger')  
logger.setLevel(logging.DEBUG)  
  
# ����һ��handler������д����־�ļ�  
fh = logging.FileHandler('test.log')  
fh.setLevel(logging.DEBUG)  
  
# �ٴ���һ��handler���������������̨  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
  
# ����handler�������ʽ  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
# ��logger���handler  
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
#except Exception, e: #���������쳣��Exception
#    print e
#    print "================="
##    traceback.print_exc()
#finally:
#    print "finally..."


