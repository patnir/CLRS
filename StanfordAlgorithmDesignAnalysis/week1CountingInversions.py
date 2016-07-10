# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 11:42:14 2016

@author: Rahul Patni
"""
import random

# Counting inversions

# Method 1: Brute Force Algorithm:

def CountingInversionsBF(A, n):
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[j] < A[i]:
                print A[j], A[i]
                inversions += 1
    return inversions

a = 6

A = [None] * a

for i in range(a):
    A[i] = random.randint(0, 100)

print A
print CountingInversionsBF(A, len(A))