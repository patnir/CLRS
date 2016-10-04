# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 21:29:42 2016

@author: Rahul Patni
"""

def better_fibonacci(n):
    if n == 0:
        return 0
        
    if n == 1:
        return 1
    
    fp = 0
    fpp = 1
    
    result = fpp + fp
    
    curr = 2
    
    while curr < n:
        fp = fpp
        fpp = result
        result = fp + fpp
        curr += 1
        
    return result
    
    