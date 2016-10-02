# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 15:00:09 2016

@author: Rahul Patni
"""

import random

# bubble sort

def bubble(A):
    lastSwap = 1
    mI = len(A) - 2
    sI = 0
    while lastSwap >= 0:
        lastSwap = -1
        for i in range(sI, mI + 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                lastSwap = i
        mI = lastSwap - 1
        for i in range(mI, sI - 1, -1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                lastSwap = i
        sI = lastSwap + 1
    print A
    checkIncreasing(A)
    return
    
    
def checkIncreasing(A):
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            print "not increasing"
            return
    print "increasing"
    return 
    
def main():
    A = []    
    for i in range(100):
        A.append(random.randint(10, 90))
    print A
    bubble(A)
    
main()