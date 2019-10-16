#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: Client.py
@Time: 2020-03-06 14:28
@Last_update: 2020-03-06 14:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from Controller import Controller


class Client(object):
    controller = Controller()
    print('Services Provided:')
    controller.get_services()
    print('Pricing for Services:')
    controller.get_pricing()


if __name__ == '__main__':
    client = Client()