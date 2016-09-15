# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 23:04:00 2016

@author: Rahul Patni
"""

# Consecutive sequence of the largest sum


import random

def largestConsecutiveSequence(A):
    if len(A) == 0:
        return None, None
    lo = A[0]
    so = 0
    eo = 0
    for i in range(len(A)):
        sc = i
        ec = i
        lc = A[i]
        curr = A[i]
        for j in range(i + 1, len(A)):
            curr += A[j]
            if curr > lc:
                lc = curr
                ec = j
        if lc > lo:
            lo = lc
            so = sc
            eo = ec
    return so, eo, lo
    
def main():
    A = []
    for i in range(0, 10):
        A.append(random.randint(-20, 20))
    A = [-12, -2, -18, 13, 10, 15, 9, -4, 10, 9]
    print A
    print largestConsecutiveSequence(A)
    i = range(5, -1, -1)
    print i

main()