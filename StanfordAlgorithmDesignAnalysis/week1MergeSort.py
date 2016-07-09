# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 20:25:57 2016

@author: Rahul Patni
"""
# Merge Sort In Python


# Merging and returning two sorted arrays
def Merge(A, B):
    n = len(A) + len(B)
    mergedArray = [None] * n
    i = 0
    j = 0    
    for k in range(n):
        print i, j
        if j == len(B) or (i < len(A) and A[i] < B[j]):
            mergedArray[k] = A[i] 
            i += 1
        else:
            mergedArray[k] = B[j]
            j += 1
    return mergedArray

print Merge([2, 3, 6, 7, 9], [1, 4, 5, 8])