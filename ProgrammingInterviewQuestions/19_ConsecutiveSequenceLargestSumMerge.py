# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 08:34:08 2016

@author: Rahul Patni
"""

# Consecutive largest sum sequence with merge routine


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
            lowSum += curr
    highSum = A[mid + 1]
    e = mid + 1
    for j in range(mid + 2, high + 1):
        curr += A[j]
        if curr > highSum:
            e = j
            highSum = curr
    return s, e, lowSum + highSum
