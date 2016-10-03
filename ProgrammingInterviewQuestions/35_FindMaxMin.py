# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 23:42:30 2016

@author: Rahul Patni
"""

# max min

import sys, random

def maxMin(A):
    big = -1 * sys.maxint
    small = sys.maxint
    
    curr = 1
    
    while curr < len(A):
        prev = curr - 1
        if A[curr] < A[prev]:
            if A[prev] > big:
                big = A[prev]
            if A[curr] < small:
                small = A[curr]
        else:
            if A[prev] < small:
                small = A[prev]
            if A[curr] > big:
                big = A[curr]
        curr += 2
    return small, big
    
    
def main():
    A = []    
    for i in range(101):
        A.append(random.randint(-100, 990))
    print A
    print maxMin(A)
    A.sort()
    print A[0], A[len(A) - 1]
    
main()