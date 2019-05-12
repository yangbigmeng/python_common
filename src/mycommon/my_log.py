#!/usr/bin python
# -*-coding:utf-8-*-
# -------------------------------------------#
# Description: 定义日志
# 
# Create on:   2019/5/12 16:46
# @author:     Marvin Yang
# @version:    1.0
# -------------------------------------------#
import logging

DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class MyLog(object):

    def __init__(self, log_name):
        # create logger
        logger = logging.getLogger(log_name)
        logger.setLevel(DEFAULT_LOG_LEVEL)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(DEFAULT_LOG_LEVEL)

        # create formatter
        formatter = logging.Formatter(DEFAULT_LOG_FORMAT)

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)
