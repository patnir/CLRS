# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:00:24 2016

@author: Rahul Patni
"""

# function to take the derivative of a polynomial


def dervative(A):
    O = [None] * (len(A) - 1)
    pow = len(A)
    for i in range(1, pow):
        O[i - 1] = A[i] * i
        
    return O

def main():
    A = [1, 2, 3, 4]
    X = dervative(A)
    print X
    
main()