# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:39:37 2016

@author: Rahul Patni
"""

# fibonnaci

def fib(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)
    
def main():
    
    print fib(4)
    
main()