# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_simple_actor_proxy.py
@Time: 2020-02-17 19:22
@Last_update: 2020-02-17 19:22
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, 'is occupied with current movies')

    def available(self):
        self.isBusy = False
        print(type(self).__name__, 'is free for the movie')

    def getState(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getState():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
