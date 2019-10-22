#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_uml_try.py
@Time: 2019-10-16 14:31
@Last_update: 2019-10-16 14:31
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Model(object):
    def logic(self):
        data = 'Got it'
        print('Model: data logic')
        return data


class View(object):
    def update(self, data):
        print('View: updating ', data)


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print('Controller: Relayed the Client')
        data = self.model.logic()
        self.view.update(data)


class Client(object):
    print('Client: asks for information')
    controller = Controller()
    controller.interface()


if __name__ == '__main__':
    client = Client()

