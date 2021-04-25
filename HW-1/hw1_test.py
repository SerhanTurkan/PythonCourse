#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import INTL_550_HW1 as hw1 

class HomeworkTest(unittest.TestCase):
    def setUp(self):
        self.portfolio = hw1.Portfolio()
        self.stock = hw1.Stock(20, "HFH")
        self.mutualFund = hw1.MutualFund("BRT")

    def test_addCash(self): 
        self.portfolio.addCash(300.50)
        self.assertEqual(300.50, self.portfolio.cash)

    def test_withdrawCash(self): 
        self.portfolio.cash = 300.50
        self.portfolio.withdrawCash(50)
        self.assertEqual(250.50, self.portfolio.cash)

    def test_buyStock(self): 
        self.portfolio.cash = 300.50
        self.portfolio.buyStock(5, self.stock)
        self.assertEqual(200.50, self.portfolio.cash)

    def test_stockAmount(self):
        self.portfolio.cash = 300.50;
        self.portfolio.buyStock(10, self.stock)
        self.portfolio.sellStock(self.stock.ticker, 4)
        self.assertEqual(6, self.portfolio.stocks[self.stock.ticker][0])

    def test_buyMutualFund(self): 
        self.portfolio.cash = 300.50
        self.assertEqual({}, self.portfolio.stocks)

    def test_sellStock(self):
        self.portfolio.cash = 300.50
        self.portfolio.buyStock(6, self.stock)
        self.portfolio.sellStock(self.stock.ticker, 4)
        self.assertEqual(2, self.portfolio.stocks[self.stock.ticker][0])

    def test_sellMutualFund(self): 
        self.portfolio.cash = 300.50
        self.portfolio.buyMutualFund(10,self.mutualFund)
        self.portfolio.sellMutualFund(self.mutualFund, 7)

if __name__ == "__main__":
    unittest.main()


# In[ ]:




