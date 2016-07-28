# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:59:44 2016

@author: Rahul Patni
"""

import random

# Maximum profit made by buying and selling a stock at the start of the day


def bruteForce(prices):
    diff = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            currDiff = prices[j] - prices[i]
            if (currDiff > diff):
                diff = currDiff
    return diff
    
    
def mainBruteForce():
    length = 5
    prices = []
    for i in range(length):
        prices.append(random.randint(0, 100))
    print prices
    diff = bruteForce(prices)
    print diff
    
mainBruteForce()