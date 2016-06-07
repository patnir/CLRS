# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 19:09:39 2016

@author: Rahul Patni
"""

import random
import sys
# MERGE SORT

def MergeSort(A, p, r):
    if p < r:
        q = (p + r) / 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        print p, q, r
        Merge(A, p, q, r)
        #print "in merge sort", A[p:r]
    print "exit p, r", p, r
    
def Merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q + 1):
        L.append(A[i])
    for j in range(q + 1, r + 1):
        R.append(A[j])
    # print "before merge", A[p:r]
    L.append(sys.maxint)
    R.append(sys.maxint)
    # print "L", L
    # print "R", R
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R [j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    # print "after merge", A[p:r]
    

size = int(raw_input("Enter size of array: "))
A = []
for i in range(size):
    A.append(random.randint(0, 100))
print "before merge sort", A

MergeSort(A, 0, size - 1)

print "after merge sort", A