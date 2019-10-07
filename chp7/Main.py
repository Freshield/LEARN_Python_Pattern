#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: Main.py
@Time: 2019-10-06 14:17
@Last_update: 2019-10-06 14:17
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from StockTrade import StockTrade
from BuyStockOrder import BuyStockOrder
from SellStockOrder import SellStockOrder
from Agent import Agent


if __name__ == '__main__':
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)