#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_real_world.py
@Time: 2020-02-29 11:49
@Last_update: 2020-02-29 11:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
class NewsPublisher(object):
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

