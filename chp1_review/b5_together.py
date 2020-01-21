# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b5_together.py
@Time: 2020-01-21 17:01
@Last_update: 2020-01-21 17:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class A(object):
    def a1(self):
        print('a1')


class B(object):
    def b(self):
        print('b')
        A().a1()


if __name__ == '__main__':
    objectB = B()
    objectB.b()