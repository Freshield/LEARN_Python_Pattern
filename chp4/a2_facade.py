# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_facade.py
@Time: 2019-09-25 19:23
@Last_update: 2019-09-25 19:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from a1_subsystem import Hotelier, Florist, Caterer, Musician


class EventManager(object):
    def __init__(self):
        print('event manager, let me talk to the folks')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class You(object):
    def __init__(self):
        print('you whoa!marriage arrangements')

    def askEventManager(self):
        print('you let\'s contact the event manager\n')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('you thanks to event manager, all preparations done!phew!')


if __name__ == '__main__':
    you = You()
    you.askEventManager()