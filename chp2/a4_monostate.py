#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a4_monostate.py
@Time: 2019-11-24 21:21
@Last_update: 2019-11-24 21:21
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
    __shared_state = {'x': 4, '1': '2'}

    def __init__(self):
        print(self.__dict__)
        self.x = 1
        print(self.__dict__)
        self.__dict__ = self.__shared_state
        pass


b = Borg()
b1 = Borg()
print(b.__dict__)
print(b1.__dict__)
b.x = 5
print(b.__dict__)
print(b1.__dict__)