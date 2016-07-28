# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:59:44 2016

@author: Rahul Patni
"""

import random
import sys
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
    length = 50
    prices = []
    for i in range(length):
        prices.append(random.randint(0, 100))
    print prices
    diff = bruteForce(prices)
    print diff
    
#mainBruteForce()


def MergeSort(A, left, right):
    if right - left == 0:
        return
    if right - left == 1:
        return A[right] - A[left]
    mid = int((left + right) / 2)
    diff = MergeSort(A, left, mid)
    nextDiff = MergeSort(A, mid + 1, right)
    next2Diff = Merge(A, left, mid, right)
    return max(max(diff, nextDiff), max(nextDiff, next2Diff))
    
def Merge(A, left, mid, right):
    B = []
    C = []
    min1 = sys.maxint
    max1 = -sys.maxint - 1
    for i in range(left, mid + 1):
        if (A[i] < min1):
            min1 = A[i]
        B.append(A[i])
    for i in range(mid + 1, right + 1):
        if (A[i] > max1):
            max1 = A[i]
        C.append(A[i])
    return max1 - min1

def mainMerge():
    length = 50
    prices = []
    for i in range(length):
        prices.append(random.randint(0, 1000))
    print prices
    print bruteForce(prices)
    result = MergeSort(prices, 0, len(prices) - 1)
    print prices
    print result
    
mainMerge()