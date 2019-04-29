# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     common.py
   Description :
   Author :       chengxingfu
   date：          2019/4/29
-------------------------------------------------
   Change Activity:
                   2019/4/29:
-------------------------------------------------
"""
import os

__author__ = 'chengxingfu'
def getLogger(logFileName):
    import logging.handlers
    logger = logging.getLogger(logFileName)
    level='INFO'
    logger.setLevel(level)
    curPath = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
    rootPath = os.sep.join(curPath.split(os.sep)[:-2])
    keepDays=3
    LOGROOT = rootPath  # "/opt/NFWD"
    if not os.path.exists(LOGROOT + "/" + "logs"):
        os.mkdir(LOGROOT + "/" + "logs")
    fh = logging.handlers.TimedRotatingFileHandler(os.path.normpath(LOGROOT + "/logs/" + logFileName), 'midnight',
                                                   backupCount=keepDays)
    fh.suffix = "%Y-%m-%d"
    fh.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger