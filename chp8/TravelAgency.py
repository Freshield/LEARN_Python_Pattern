#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: TravelAgency.py
@Time: 2019-10-13 13:26
@Last_update: 2019-10-13 13:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from VeniceTrip import VeniceTrip
from MaldivesTrip import MaldivesTrip


class TravelAgency(object):
    def arrange_trip(self, choice):
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


if __name__ == '__main__':
    TravelAgency().arrange_trip('beach')
