#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: VeniceTrip.py
@Time: 2019-10-12 13:21
@Last_update: 2019-10-12 13:21
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


class VeniceTrip(Trip):
    def setTransport(self):
        print('venice transport')

    def day1(self):
        print('venice day1')

    def day2(self):
        print('venice day2')

    def day3(self):
        print('venice day3')

    def returnHome(self):
        print('venice return home')

