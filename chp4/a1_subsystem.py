# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_subsystem.py
@Time: 2020-02-15 19:19
@Last_update: 2020-02-15 19:19
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Hotelier(object):
    def __init__(self):
        print('arranging the hotel for marriage')

    def __isAvailable(self):
        print('is the hotel free for the event on given day')
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print('registered the booking\n')


class Florist(object):
    def __init__(self):
        print('flower decorations for the vent')

    def setFlowerRequirements(self):
        print('carnations, roses and lilies would be used for decorations\n')


class Caterer(object):
    def __init__(self):
        print('food arrangements for the envent')

    def setCuisine(self):
        print('chinese & continental cuisine to be served\n')


class Musician(object):
    def __init__(self):
        print('musical arrangements for the marriage')

    def setMusicType(self):
        print('jazz and classical will be played\n')