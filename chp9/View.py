#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: View.py
@Time: 2020-03-06 14:24
@Last_update: 2020-03-06 14:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from Model import Model


class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print('For', Model.services[svc]['number'],
                  svc, 'message you pay $',
                  Model.services[svc]['price'])