# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 20:25:57 2016

@author: Rahul Patni
"""
# Merge Sort In Python


# Merging and returning two sorted arrays
def MergeTwoArrays(A, B):
    n = len(A) + len(B)
    mergedArray = [None] * n
    i = 0
    j = 0    
    for k in range(n):
        if j == len(B) or (i < len(A) and A[i] < B[j]):
            mergedArray[k] = A[i] 
            i += 1
        else:
            mergedArray[k] = B[j]
            j += 1
    return mergedArray

def Merge(A, p, q, r):
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
    for k in range(p, r + 1):
        if j == len(C) or (i < len(B) and B[i] < C[j]):
            A[k] = B[i] 
            i += 1
        else:
            A[k] = C[j]
            j += 1
    return A

def MergeSort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
    return A

print MergeTwoArrays([1, 4, 5, 8], [2, 3, 6, 7, 9])
print Merge([100, 6, 7, 8, 9, 1, 2, 3, 4, 5, 120], 1, 4, 9)
A = [1, 4, 5, 2, 3, 6, 7, 8, 9]
print MergeSort(A, 0, len(A) - 1)