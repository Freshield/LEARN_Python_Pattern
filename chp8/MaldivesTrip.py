#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: MaldivesTrip.py
@Time: 2019-10-13 13:25
@Last_update: 2019-10-13 13:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from Trip import Trip


class MaldivesTrip(Trip):
    def setTransport(self):
        print('maldives transport')

    def day1(self):
        print('maldives day1')

    def day2(self):
        print('maldives day2')

    def day3(self):
        print('maldives day3')

    def returnHome(self):
        print('maldives return home')


