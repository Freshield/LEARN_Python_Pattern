#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_simple_try.py
@Time: 2020-03-04 11:23
@Last_update: 2020-03-04 11:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print('copying binaries --', self.src, ' to ', self.rootdir)
            else:
                print('no operation')


if __name__ == '__main__':
    wizard = Wizard('python3.5.gzip', '/usr/bin/')
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()