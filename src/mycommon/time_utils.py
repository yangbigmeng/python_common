#!/usr/bin/python
# -*-coding:utf-8-*-
# -------------------------------#
# FileName:    TimeUtils.py
# Description: 时间基本处理函数
#
# Create on:   2018/6/9 17:23
# Author:      Marvin Yang
# -------------------------------#

import time
import types


class TimeUtils(object):

    @staticmethod
    def time2timestamp(time_str, time_format="%Y-%m-%d %H:%M:%S"):
        """
            时间转换为时间戳

            :param time_str: 时间字符串
            :param time_format: 时间格式
            :return: 时间戳
            """
        assert isinstance(time_str, types.StringType)
        return time.mktime(time.strptime(time_str, time_format))

    @staticmethod
    def timestamp2time(timestamp, time_format="%Y-%m-%d %H:%M:%S"):
        """
        时间戳转换为时间字符串

        :param timestamp: 时间戳
        :param time_format: 时间格式
        :return: 时间字符串
        """
        assert isinstance(timestamp, types.FloatType) or isinstance(timestamp, types.IntType)
        return time.strftime(time_format, time.localtime(timestamp))


if __name__ == "__main__":

    #test time2timestamp
    a = "2018-06-09 17:44:45"
    print TimeUtils.time2timestamp(a)

    # test timestamp2time
    b = 152853748
    print TimeUtils.timestamp2time(b)
