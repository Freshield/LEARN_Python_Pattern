# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_real_world.py
@Time: 2020-02-22 23:26
@Last_update: 2020-02-22 23:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print('Bank: checking if account has enought funds')
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print('bank paying the merchant')
            return True
        else:
            print('bank sorry, not enough funds')
            return False


class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = 'card number'
        self.bank.setCard(card)
        return self.bank.do_pay()


class You(object):

    def __init__(self):
        print('you lets buy the denim shirt')
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print('you wow!denim shirt is Mine')
        else:
            print('you I should earn more')


if __name__ == '__main__':
    you = You()
    you.make_payment()


