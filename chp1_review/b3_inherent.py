#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_inherent.py
@Time: 2020-01-25 11:32
@Last_update: 2020-01-25 11:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class A:
    def a1(self):
        print('a1')


class B(A):
    def b(self):
        print('b')


if __name__ == '__main__':
    b = B()
    b.a1()