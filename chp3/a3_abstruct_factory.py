# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a3_abstruct_factory.py
@Time: 2019-09-19 12:51
@Last_update: 2019-09-19 12:51
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


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndiaPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanBgPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, NonVegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('prepare ', type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self):
        print('served with chicken ', type(self).__name__)


class MexicanBgPizza(VegPizza):
    def prepare(self):
        print('prepare ', type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self):
        print('served with Ham ', type(self).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndiaPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve()


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.makePizzas()