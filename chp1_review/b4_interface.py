# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_interface.py
@Time: 2020-01-22 16:58
@Last_update: 2020-01-22 16:58
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Adder:
    def __init__(self):
        self.sum = 0

    def add(self, value):
        self.sum += value


if __name__ == '__main__':
    acc = Adder()
    for i in range(99):
        acc.add(i)

    print(acc.sum)