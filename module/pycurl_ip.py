# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

import pycurl


def info():
    return "info"


def poc(str):
    # As long as the file is opened in binary mode, both Python 2 and Python 3
    # can write response body to it without decoding.
    with open(str + '.html', 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://' + str)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()

    return True


def exp():
    return "exp"