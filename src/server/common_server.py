#!/usr/bin/python
# -*-coding:utf-8-*-
# -------------------------------#
# FileName:    CommonServer.py
# Description:
# Create on:   2018/6/9 18:12
# Author:      Marvin Yang
# -------------------------------#
import logging
import os
import sys
import time
import traceback

import tornado.ioloop
import tornado.web
from tornado.escape import json_encode

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from service.common_handler import CommonHandler
from mysetting import COMMON_SERVER_PORT


class JsonEncoder(object):

    @staticmethod
    def common_response(result, cost_time):
        """
        正常返回结果

        :param result: 返回结果
        :param cost_time: 耗时
        :return: json_str
        """
        header = {"cost_time": cost_time, "msg": "ok", "status": 0, "response": result}
        return json_encode(header)

    @staticmethod
    def error_response(result, msg, cost_time):
        """
        处理异常返回结果

        :param result: 返回结果
        :param msg: 错误信息
        :param cost_time: 耗时
        :return: json_str
        """
        header = {"cost_time": cost_time, "msg": msg, "status": -1, "response": result}
        return json_encode(header)


class Handler(tornado.web.RequestHandler):
    def initialize(self, handler):
        self.handler = handler

    def get(self, *args, **kwargs):
        start_time = time.time()
        try:
            params = self.get_argument("params")
            pro_type = self.get_argument("type", "time2timestamp")
            flag, result = self._process(params, pro_type)
            result_str = JsonEncoder.common_response(result, time.time() - start_time)
        except Exception as e:
            logging.error(traceback.format_exc())
            result_str = JsonEncoder.error_response(None, str(e), time.time() - start_time)
        self.write(result_str)

    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json")
        start_time = time.time()
        try:
            params = self.get_argument("params")
            pro_type = self.get_argument("type", "time2timestamp")
            flag, result = self._process(params, pro_type)
            result_str = JsonEncoder.common_response(result, time.time() - start_time)
        except Exception as e:
            logging.error(traceback.format_exc())
            result_str = JsonEncoder.error_response(None, str(e), time.time() - start_time)
        self.write(result_str)

    def _process(self, params, process_type):
        """
        实际处理方法

        :param params: 请求参数
        :param process_type: 处理类型
        :return: True, result
        """
        return self.handler.process(params, process_type)


class CommonServer(object):
    def __init__(self, handler, sever_port, env="TEST"):
        self.env = env
        self.common_handler = handler
        self.server_port = sever_port

    def load(self):
        return tornado.web.Application([(r"/common", Handler, dict(handler=self.common_handler)), ], autoreload=False)

    def process(self, ):
        common_app = self.load()
        common_app.listen(self.server_port)
        tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    env_type = "TEST"
    if len(sys.argv) > 1:
        env_type = sys.argv[0]

    # common server
    common_handler = CommonHandler()
    obj = CommonServer(common_handler, COMMON_SERVER_PORT, env_type)
    print obj.load()
    obj.process()
