# -*- coding: utf-8 -*-
"""
Created on Sat Jul 09 17:26:00 2016

@author: Rahul Patni
"""

# Alternate approach to multiply two numbers:
import math 

# multiplying two numbers with the same number of digits
def recMul(x, y):
    digits = numberOfDigits(x)
    
    # base case: when both numbers are single digit
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
    
    result = int(math.pow(10, digits) * recMul(a, c) + math.pow(10, digits / 2) * (recMul(a, d) + recMul(b, c)) + recMul(b, d))
    
    return result

def numberOfDigits(x):
    count = 1
    x = x / 10
    while (x > 0):    
        count += 1
        x = x / 10
    
    return count
    
print recMul(56, 78)