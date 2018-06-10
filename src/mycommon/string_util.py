#!/usr/bin/python
#-*-coding:utf-8-*-
#-------------------------------#
# FileName:    string_util.py
# Description: 字符串处理函数
#
# Author:      yangmeng(eyangmeng@163.com)
#-------------------------------#

import types


def get_utf(string):
    if isinstance(string, types.UnicodeType):
        string = string.encode("utf-8")
    return string


def get_unicode(string):
    if isinstance(string, types.StringType):
        string = string.decode("utf-8")
    return string


def is_chinese(u_char):
    return u_char >= u"\u4e00" and not u_char > u"\u9fff"


if __name__ == "__main__":
    ch = u"中"
    print is_chinese(ch)
