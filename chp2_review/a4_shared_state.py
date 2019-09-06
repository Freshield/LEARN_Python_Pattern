# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_shared_state.py
@Time: 2019-09-03 14:16
@Last_update: 2019-09-03 14:16
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


class Borg1:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg1, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


if __name__ == '__main__':
    b = Borg1()
    b1 = Borg1()
    b.x = 4

    print(b)
    print(b1)
    print(b.__dict__)
    print(b1.__dict__)