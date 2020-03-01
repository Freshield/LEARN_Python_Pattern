#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_simple_subject.py
@Time: 2020-03-03 10:40
@Last_update: 2020-03-03 10:40
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Subject(object):
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            print(type(self).__name__)
            observer.notify(self, *args)


class Observer1(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ' got ', args, 'from', subject)


class Observer2(object):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ' got ', args, 'from', subject)


if __name__ == '__main__':
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)

    subject.notifyAll('notification')
