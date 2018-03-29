#!/usr/bin/python
# -*- coding:utf-8 -*- 


def log(func):
    def _log(*args, **kwargs):
        # print "[log]go into %s\n"%func.__name__
        res = func(*args, **kwargs)
        # print "[log]go outfo %s\n"%func.__name__
        return res
    return _log
