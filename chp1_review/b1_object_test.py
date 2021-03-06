#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_object_test.py
@Time: 2020-01-27 11:20
@Last_update: 2020-01-27 11:20
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return '<Person (%s, %s)>' % (self.name, self.age)


if __name__ == '__main__':
    p = Person('John', 32)
    print('Type of Object:', type(p))
    print(p.get_person())