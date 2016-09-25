# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 10:29:52 2016

@author: Rahul Patni
"""

# Dynamic Programming Fibonacci

def recursiveApproach(n):
    if n == 0 or n == 1:
        return 1
    return recursiveApproach(n - 1) + recursiveApproach(n - 2)
    
def iterativeApproach(n):
    x1 = 0
    x2 = 1
    for i in range(1, n + 1):
        x3 = x1 + x2
        x1 = x2
        x2 = x3
    return x2
    
def dynamicApproach(n):
    fib = dict()
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    # print fib
    return fib[n]
    
    
def main():
    x = 10
    print recursiveApproach(x)
    print iterativeApproach(x)
    print dynamicApproach(x)
    
main()