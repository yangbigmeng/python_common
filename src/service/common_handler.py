#!/usr/bin/python
# -*-coding:utf-8-*-
# -------------------------------#
# FileName:    common_handler.py
# Description: 基本处理handler
#
# Create on:   2018/6/9 18:10
# Author:      Marvin Yang
# -------------------------------#

import logging
import os
import sys
import traceback

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from mycommon.time_utils import TimeUtils


class CommonHandler(object):
    def __init__(self, env="TEST"):
        self.env = env

    @staticmethod
    def load():
        return True, "ok"

    @staticmethod
    def time2timestamp_process(time_str):
        """
        时间字符串转换为时间戳

        :param time_str: 时间字符串
        :return: 时间戳
        """
        if not time_str:
            return None
        return {"timestamp": TimeUtils.time2timestamp(str(time_str))}

    @staticmethod
    def timestamp2time_process(timestamp):
        """
        时间戳转换为时间字符串

        :param timestamp: 时间戳
        :return: 时间字符串
        """
        if not timestamp:
            return None
        return {"time_str": TimeUtils.timestamp2time(float(timestamp))}

    def process(self, params, process_type):
        """
        根据process_type进行相应的处理操作

        :param params: 参数
        :param process_type: 操作类型
            (1) time2timestamp
            (2) timestamp2time
        :return: True, result:{k-v},
        """
        function_name = "%s_process" % process_type
        try:
            return True, getattr(self, function_name)(params)
        except Exception as e:
            logging.error(traceback.format_exc())
            return False, str(e)


if __name__ == "__main__":
    env_type = "TEST"
    if len(sys.argv) > 1:
        env_type = sys.argv[0]
    obj = CommonHandler(env_type)
    print obj.load()

    # test
    u_time_str = "2018-06-09 17:44:45"
    pro_type = "time2timestamp"
    print obj.process(u_time_str, pro_type)
