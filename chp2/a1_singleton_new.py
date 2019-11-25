#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_singleton_new.py
@Time: 2019-11-24 20:52
@Last_update: 2019-11-24 20:52
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

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(s)
s1 = Singleton()
print(s1)