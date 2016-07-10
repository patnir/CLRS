# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 11:42:14 2016

@author: Rahul Patni
"""
import random

# Counting inversions for an array with distinct elements

# Method 1: Brute Force Algorithm:

def CountingInversionsBF(A, n):
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[j] < A[i]:
                inversions += 1
    return inversions


def CountAndMerge(A, p, q, r):
    B = [None] * (q - p + 1)
    C = [None] * (r - q)
    k = 0
    for i in range(p, q + 1):
        B[k] = A[i]
        k += 1
    k = 0
    for i in range(q + 1, r + 1):
        C[k] = A[i]
        k += 1
    i = 0
    j = 0
    inversions = 0
    for k in range(p, r + 1):
        if j == len(C) or (i < len(B) and B[i] <= C[j]):
            A[k] = B[i] 
            i += 1
        else:
            A[k] = C[j]
            if i < len(B):
                inversions += len(range(i, len(B)))
            j += 1
    return A, inversions

def CountAndSort(A, p, r):
    x = 0
    y = 0
    z = 0
    if p < r:
        q = int((p + r) / 2)
        A, x = CountAndSort(A, p, q)
        A, y = CountAndSort(A, q + 1, r)
        A, z = CountAndMerge(A, p, q, r)
    return B, x + y + z

a = 100

A = [None] * a

for i in range(a):
    A[i] = random.randint(0, 100)
B = A
print A
print B
print CountingInversionsBF(A, len(A))

print CountAndSort(B, 0, len(B) - 1)[1]

