# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 17:26:00 2016

@author: Rahul Patni
"""

# Alternate approach to multiply two numbers:
import math 

def recMul(x, y):
    if x < y:
        digits = numberOfDigits(y)
    else:
        digits = numberOfDigits(x)
    
    if digits == 1:
        return int(x * y)
    
    a = int(x / math.pow(10, digits / 2))
    print "a", a
    b = int(x % math.pow(10, digits / 2))
    print "b", b
    c = int(y / math.pow(10, digits / 2))
    print "c", c
    d = int(y % math.pow(10, digits / 2))
    print "d", d
    
    ac = recMul(a, c)
    bd = recMul(b, d)
    adPcb = recMul(a + b, c + d) - ac - bd # sum of (ad + bc) = (a+b) * (c + d) - ac - bd
    
    result = int(math.pow(10, digits) * ac + math.pow(10, digits / 2) * adPcb + bd)
    
    return result

def numberOfDigits(x):
    count = 1
    x = x / 10
    while (x > 0):    
        count += 1
        x = x / 10
    
    return count
    
print recMul(4, 567)