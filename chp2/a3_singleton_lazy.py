#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_singleton_lazy.py
@Time: 2019-11-24 21:11
@Last_update: 2019-11-24 21:11
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
    instance = None

    def __init__(self):
        if not Singleton.instance:
            print('__init__ method called..')
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        print('lol')
        if not cls.instance:
            print('here')
            cls.instance = Singleton()
        return cls.instance


s = Singleton()
print(s)
print()
print(Singleton.instance)
print()
Singleton.getInstance()
print()
print(Singleton.instance)
print()
s1 = Singleton()
print(s1)