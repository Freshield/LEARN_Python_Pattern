# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_module.py
@Time: 2019-09-02 13:11
@Last_update: 2019-09-02 13:11
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a3_m1_model import Singleton

a = Singleton
a.test = 1

b = Singleton
print(b.test)