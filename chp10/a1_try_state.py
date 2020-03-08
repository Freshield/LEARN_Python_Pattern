# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_try_state.py
@Time: 2020-03-07 21:41
@Last_update: 2020-03-07 21:41
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
    def Handle(self):
        pass


class ConcreteStateB(State):
    def Handle(self):
        print('ConcreteStateB')


class ConcreteStateA(State):
    def Handle(self):
        print('ConcreteStateA')


class Context(State):

    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def Handle(self):
        self.state.Handle()


context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()

context.setState(stateA)
context.Handle()
