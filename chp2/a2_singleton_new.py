#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_singleton_new.py
@Time: 2019-11-24 21:01
@Last_update: 2019-11-24 21:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Singleton(object):
    _singleon = None

    def __new__(cls, *args, **kwargs):
        if cls._singleon is None:
            cls._singleon = object.__new__(cls, *args, **kwargs)

        return cls._singleon



s = Singleton()
print(s)
s1 = Singleton()
print(s1)