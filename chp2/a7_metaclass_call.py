#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a7_metaclass_call.py
@Time: 2019-11-25 21:34
@Last_update: 2019-11-25 21:34
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class MetaSingleton(type):
    instance = None

    def __init__(cls, *args, **kwargs):
        print('here1')
        print(*args)
        print(**kwargs)

    def __new__(mcs, *args, **kwargs):
        print('here')
        return type.__new__(mcs, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print(cls.instance)
        if cls.instance is None:
            cls.instance = type.__call__(cls, *args, **kwargs)

        return cls.instance


class Logger(metaclass=MetaSingleton):

    def __init__(self):
        print('init')

    def __new__(cls, *args, **kwargs):
        print('new')
        return super(Logger, cls).__new__(cls)

l1 = Logger()
print(l1)