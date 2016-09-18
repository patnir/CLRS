# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 08:34:08 2016

@author: Rahul Patni
"""

# Consecutive largest sum sequence with merge routine

import random

def Merge(A, s, e):
    if s == e:
        return s, e, A[e]
    if s < e:
        mid = (s + e) / 2
        a = Merge(A, s, mid)
        b = Merge(A, mid + 1, e)
        c = MaxCrossingSubarray(A, s, mid, e)
        maxS = a
        if maxS[2] < b[2]:
            maxS = b
        if maxS[2] < c[2]:
            maxS = c
        return maxS

def MaxCrossingSubarray(A, low, mid, high):
    s = mid
    lowSum = A[mid]
    curr = A[mid]
    for i in range(mid - 1, low - 1, -1):
        curr += A[i]
        if curr > lowSum:
            s = i
            lowSum = curr
    highSum = A[mid + 1]
    curr = highSum
    e = mid + 1
    for j in range(mid + 2, high + 1):
        curr += A[j]
        if curr > highSum:
            e = j
            highSum = curr
    return s, e, lowSum + highSum

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

def maxContSub(A):
    m = A[0]
    curr = A[0]
    
    for i in range(1, len(A)):
        curr += A[i]
        if A[i] > curr:
            curr = A[i]
        if curr < 0 and m > 0:
            curr = 0
        if curr > m:
            if A[i] > curr:
                curr = A[i]
            m = curr
    return m
            
            

def main():
    A = []
    for i in range(10):
        A.append(random.randint(-30, 30))
    #[-29, -21, 4, 5, -26, -29, -27, -29, -2, -23]
    #[-22, -9, -1, 10, -22, 8, 23, -5, -7, -25]
        
    A = [-22, -9, -1, 10, -22, 8, 23, -5, -7, -25]
    A = [-8, -7, -6, -5, -5, -3]
    print A
    print largestConsecutiveSequence(A)
    print Merge(A, 0, len(A) - 1)
    print maxContSub(A)
    
    return
    
main()