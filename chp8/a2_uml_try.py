#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_uml_try.py
@Time: 2019-10-11 11:27
@Last_update: 2019-10-11 11:27
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


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print('defining the algorithm. operation1 follows operation2')
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):

    def operation1(self):
        print('my concrete opertaion1')

    def operation2(self):
        print('operation 2 remains same')


class Client(object):
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()


if __name__ == '__main__':
    client = Client()
    client.main()