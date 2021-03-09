#!/usr/bin/env python
# coding: utf-8

# Serhan TÜRKAN
# <br>
# INTL550 HomeWork1

# In[1]:


import random
from datetime import datetime

class Portfolio(object):
    def __init__(self):
        self.cash = 0.00
        self.stocks = {}
        self.mutualFunds = {}
        self.log = {}
        self.addLog("Portfolio has been created")
        
    def __str__(self):
        return "Cash: {}\nStocks: {}\nMutual Funds: {}".format(self.cash, self.stocks, self.mutualFunds)
    
    def addLog(self, text):
        now = datetime.now()
        logtime = now.strftime("%d/%m/%Y %H:%M:%S")
        #self.log["{}".format(logtime)] = text
        self.log["{} - {}".format(len(self.log),logtime)] = text
    def history(self):
        return self.log
    
    def addCash(self, amount):
        self.cash += amount
        self.addLog("${} added, Cash Balance: ${}".format(amount,self.cash ))
        
    def withdrawCash(self, amount):
        self.cash -= amount
        self.addLog("${} withdrawn, Cash Balance: ${}".format(amount,self.cash ))
    
    def buyMutualFund(self, amount, mf):
        cost = amount
        if cost > self.cash:
            print("Insufficient balance - Available: {} / Required: {} ".format(self.cash,cost))
        else:
            self.cash -= cost
            if mf.ticker in self.mutualFunds:
                self.mutualFunds[mf.ticker] = (self.mutualFunds[mf.ticker][0] + amount, cost)
            else:
                self.mutualFunds[mf.ticker] = (amount, cost)
            print("You bought: {} shares of {} mutual fund. ".format(amount,mf.ticker))
            self.addLog("Bought {} shares of {} for {} dollars. Cash Balance: ${}".format(amount,mf.ticker,cost ,self.cash ))
    
    def sellMutualFund(self, ticker, amount):
        if ticker in self.mutualFunds.keys():
            if self.mutualFunds[ticker][0] >= amount:
                received = random.uniform(0.9,1.2) * amount * self.mutualFunds[ticker][1]
                self.cash += received
                self.mutualFunds[ticker] = (self.mutualFunds[ticker][0] - amount, self.mutualFunds[ticker][1])
                print("You sold: {} shares of {} mutual fund. ".format(amount,ticker))
                self.addLog("Sold {} shares of {} for {} dollars. Cash Balance: ${}".format(amount,ticker,received,self.cash))
            else: 
                print("You don't have that much funds")
        else:
            print("Please enter a valid fund ticker.")          
        
    def buyStock(self, amount, stock):
        cost = stock.price * amount
        if cost > self.cash:
            print("Insufficient balance - Available: {} / Required: {} ".format(self.cash,cost))
        else:
            self.cash -= cost
            if stock.ticker in self.stocks:
                presentAmount = self.stocks[stock.ticker][0]
                averagedCost = ((presentAmount * self.stocks[stock.ticker][1]) + (amount * stock.price)) / (presentAmount + amount)
                self.stocks[stock.ticker] = (self.stocks[stock.ticker][0] + amount, averagedCost)
                
            else:
                self.stocks[stock.ticker] = (amount, stock.price)
            print("You bought: {} shares of {} stock. ".format(amount,stock.ticker))
            self.addLog("Bought {} shares of {} for {} dollars. Cash Balance: ${}".format(amount,stock.ticker,cost ,self.cash ))
            
    def sellStock(self, ticker, amount):
        if ticker in self.stocks.keys():
            if self.stocks[ticker][0] >= amount:
                received = random.uniform(0.5,1.5) * amount * self.stocks[ticker][1]
                self.cash += received
                self.stocks[ticker] = (self.stocks[ticker][0] - amount, self.stocks[ticker][1])
                print("You sold: {} shares of {} stock. ".format(amount,ticker))
                self.addLog("Sold {} shares of {} for {} dollars. Cash Balance: ${}".format(amount,ticker,received,self.cash))
            else: #wrong amount
                print("You don't have that much stock")
        else:
            print("Please enter a valid stock ticker.")
         
class Stock(object):
    def __init__(self, price, ticker):
        self.price = price
        self.ticker = ticker

class MutualFund(object):
    def __init__(self, ticker):
        self.ticker = ticker


# In[2]:


portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio
#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT
# 2 GHT
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions
#ordered by time

