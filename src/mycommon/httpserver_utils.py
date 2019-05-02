#!/usr/bin/python
# -*-coding:utf-8-*-
# -------------------------------#
# FileName:    HttpserverUtils.py
# Description: httpserver 基本操作
# 
# Create on:   2018/6/9 19:44
# Author:      Marvin Yang
# -------------------------------#

import json
import logging
import sys
import traceback
import urllib
import urllib2


class HttpserverUtils(object):
    def __init__(self, env="TEST"):
        self.env = env

    def load(self):
        return True, "ok"

    @staticmethod
    def post(url, params):
        """
        post请求处理

        :param url: 请求url
        :param params: 参数数据
        :return: True, result
        """
        try:
            data = urllib.urlencode(params)
            request = urllib2.Request(url)
            result = urllib2.urlopen(request, data, timeout=10).read()
            return True, json.loads(result)
        except Exception as e:
            logging.warn(traceback.format_exc())
            return False, str(e)

    @staticmethod
    def get(url, params):
        """
        get请求

        :param url: 请求url
        :param params: 请求参数
        :return: True, result
        """
        try:
            data = urllib.urlencode(params)
            req_url = url + data
            result = urllib2.urlopen(req_url, timeout=10).read()
            return True, json.loads(result)
        except Exception as e:
            logging.warn(traceback.format_exc())
            return False, str(e)

    def process(self, ):
        pass


if __name__ == "__main__":
    env_type = "TEST"
    if len(sys.argv) > 1:
        env_type = sys.argv[0]
    obj = HttpserverUtils(env_type)
    print obj.load()

    # test get
    url = "http://localhost:12358/common?"
    params = {"params": "1528516800", "type": "timestamp2time"}
    print obj.get(url, params)

    # test post
    url = "http://localhost:12358/common?"
    params = {"params": "1528516800", "type": "timestamp2time"}
    print obj.post(url, params)
