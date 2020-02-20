#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a2_real_world.py
@Time: 2020-02-29 11:49
@Last_update: 2020-02-29 11:49
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


class NewsPublisher(object):
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subseribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return 'got news:', self.__latestNews


class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for sub in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        sub(news_publisher)
    print('subscribers:', news_publisher.subseribers())

    news_publisher.addNews('Hello World!')
    news_publisher.notifySubscribers()

    print('detached:', type(news_publisher.detach()).__name__)
    print('subscribers:', news_publisher.subseribers())

    news_publisher.addNews('My second news!')
    news_publisher.notifySubscribers()


