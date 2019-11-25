#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a5_monostate_new.py
@Time: 2019-11-25 20:26
@Last_update: 2019-11-25 20:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Borg(object):
    shared_state = {'y': 2}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls)
        obj.x = 1
        obj.__dict__ = cls.shared_state
        return obj


b = Borg()
print(b.__dict__)
print(b.shared_state)
b1 = Borg()
b1.y = 3
print(b.__dict__)
print(b1.__dict__)