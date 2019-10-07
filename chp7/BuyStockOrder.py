#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: BuyStockOrder.py
@Time: 2019-10-06 14:13
@Last_update: 2019-10-06 14:13
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from Order import Order


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
        
    def execute(self):
        self.stock.buy()

