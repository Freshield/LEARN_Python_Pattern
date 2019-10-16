#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: Controller.py
@Time: 2020-03-06 14:26
@Last_update: 2020-03-06 14:26
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
from View import View


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return (self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys()
        return (self.view.list_pricing(services))

