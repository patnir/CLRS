# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:21:36 2016

@author: Rahul Patni
"""

def number_needed(a, b):
    array1 = [0] * 26
    array2 = [0] * 26
    for i in a:
        array1[ord(i) - ord('a')] += 1
    for i in b:
        array2[ord(i) - ord('a')] += 1
    total = 0
    for i in range(0, 26):
        total += abs(array1[i] - array2[i])
        
    return total

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
