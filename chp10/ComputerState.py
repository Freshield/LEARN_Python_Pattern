# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: ComputerState.py
@Time: 2020-03-08 21:31
@Last_update: 2020-03-08 21:31
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class ComputerState(object):
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switched to', state.name, ' not possible.')

    def __str__(self):
        return self.name
