#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_test_star.py
@Time: 2019-11-24 21:09
@Last_update: 2019-11-24 21:09
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def foo(*args):
    print(args)
    print(*args)



foo(1,2,3,4,5)