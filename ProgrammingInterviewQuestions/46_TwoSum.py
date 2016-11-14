# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 08:35:26 2016

@author: Rahul Patni
"""

# 2 sum of sorted array

import random

def check(A, target):
    B = list(A)
    for i in range(len(A)):
        B[i] = target - B[i] 
    print A
    i = 0
    j = len(A) - 1
    print B
    while (j >= 0 and i < len(A)):
        if B[j] == A[i]:
            print "combo is", B[j], 7 - B[j]
            return
        if B[j] > A[i]:
            i+= 1
        else:
            j -= 1
    print "not found"
    return

def main():
    size = 5
    A = [0] * size
    for i in range(size):
        val = random.randint(0, size)
        A[i] = val
    A.sort()
    check(A, 7)
    return
    
main()