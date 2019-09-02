# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_singleton.py
@Time: 2019-08-30 12:01
@Last_update: 2019-08-30 12:01
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
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance


if __name__ == '__main__':
    s = Singleton()
    print('object created', s)
    s.test = 1

    s1 = Singleton()
    print('object created', s1)
    print(s1.test)

    s1.test = 2
    print(s.test)