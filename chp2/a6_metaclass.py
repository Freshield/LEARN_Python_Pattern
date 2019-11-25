#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a6_metaclass.py
@Time: 2019-11-25 20:56
@Last_update: 2019-11-25 20:56
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
        print(*args)
        print('do you want')
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        print('here1')
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        print('here')


i = int(4, 5)
i()