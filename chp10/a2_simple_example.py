#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: a2_simple_example.py
@Time: 2020-03-08 18:26
@Last_update: 2020-03-08 18:26
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


class State(metaclass=ABCMeta):

    @abstractmethod
    def doThis(self):
        pass


class StartState(State):
    def doThis(self):
        print('TV Switching ON...')


class StopState(State):
    def doThis(self):
        print('TV Switching OFF...')


class TVContext(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()


context = TVContext()
context.getState()

start = StartState()
stop = StopState()

context.setState(stop)
context.doThis()