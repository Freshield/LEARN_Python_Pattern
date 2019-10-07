#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: Order.py
@Time: 2019-10-06 14:12
@Last_update: 2019-10-06 14:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


