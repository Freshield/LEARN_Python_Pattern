# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: Computer.py
@Time: 2020-03-08 21:40
@Last_update: 2020-03-08 21:40
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from States import *


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()

    comp.change(On)
    comp.change(Off)

    comp.change(On)
    comp.change(Suspend)

    comp.change(Hibernate)

    comp.change(On)
    comp.change(Off)