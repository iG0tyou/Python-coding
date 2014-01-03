#!/usr/bin/python
#_*_ coding:UTF-8 _*_

import os
import time
import logging as log
import logging
import logging.handlers


__author__ = 'sunlzx'

BASE_HOME = "R:/TEMP"
LOG_DIRS = ["log", "logs"]
SAVE_DAYS = 30
DAY = 24 * 3600




LOG_FILE = 'del_log.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter

log = logging.getLogger('del_log')    # 获取名为tst的logger
log.addHandler(handler)           # 为logger添加handler
log.setLevel(logging.DEBUG)


def formatDateTime(seconds):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(seconds))


def delelteLog(dir, logDirs, minTimeStamp):
    if os.path.isdir(dir):
        for logDir in logDirs:
            dirPath = dir + "/" + logDir
            if not os.path.isdir(dirPath):
                continue;
            for fileName in os.listdir(dirPath):
                filePath = dirPath + "/" + fileName
                print filePath
                lastModifyTime = os.path.getmtime(filePath);
                if lastModifyTime < minTimeStamp:
                    if os.path.isfile(filePath):
                        log.info("delete file:" + filePath)
                        os.remove(filePath)



dirs = os.listdir(BASE_HOME)

minTimeStamp = time.time() - SAVE_DAYS * DAY;
print formatDateTime(minTimeStamp)
print("xxx " + str(1))
for dir in dirs:
    absPath = BASE_HOME + "/" + dir;
    log.info("checking dir:" + absPath)
    delelteLog(absPath, LOG_DIRS, minTimeStamp)
