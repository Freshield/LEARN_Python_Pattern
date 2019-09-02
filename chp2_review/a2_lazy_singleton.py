# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_lazy_singleton.py
@Time: 2019-09-01 12:58
@Last_update: 2019-09-01 12:58
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            print('init called')
        else:
            print('already created', self.getInstance())

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            print('here')
            cls.__instance = Singleton()
            print('here1')
        return cls.__instance


if __name__ == '__main__':
    s = Singleton()
    print('cretaed', Singleton.getInstance())

    s1 = Singleton()