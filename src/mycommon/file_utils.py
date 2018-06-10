#!/usr/bin/python
# -*-coding:utf-8-*-
# -------------------------------#
# FileName:    file_utils.py
# Description: 文件处理基本函数
#
# Create on:   2018/6/9 17:24
# Author:      yangmeng(eyangmeng@163.com)
# -------------------------------#

import json
import os


def file_iterator(file_name):
    """
    读取文件中的内容, 返回迭代器

    :param file_name: 文件名, 文件格式为一行为一条数据
    """
    assert os.path.exists(file_name)
    with open(file_name, "r") as r_file:
        line = r_file.readline()
        while True:
            if not line:
                break
            yield line.strip()
            line = r_file.readline()


def json_file_iterator(file_name):
    """
    读取文件中的内容, 返回迭代器

    :param file_name: 文件名, 文件格式为一行为一条json数据
    """
    assert os.path.exists(file_name)
    with open(file_name, "r") as r_file:
        line = r_file.readline()
        while True:
            if not line:
                break
            yield json.loads(line.strip())
            line = r_file.readline()

