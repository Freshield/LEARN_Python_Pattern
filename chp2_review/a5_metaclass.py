# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_metaclass.py
@Time: 2019-09-06 14:32
@Last_update: 2019-09-06 14:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print('here is my int', args)
        print('now do')
        return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)