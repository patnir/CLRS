# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 11:46:39 2016

@author: Rahul Patni
"""

# quick sort implementation

# A : array to be sorted
# n : length of the array to be sorted

def ChoosePivot(A):
    # For now, returning 1
    return 0

def QuickSort(A):
    if len(A) <= 1:
        return A
    p = ChoosePivot(A)
    B = []
    C = []
    print A
    for i in A:
        if i < A[p]:
            B.append(i)
    for i in A:
        if i > A[p]:
            C.append(i)
    B = QuickSort(B)
    C = QuickSort(C)
    J = []
    [J.append(x) for x in B]
    J.append(A[p])
    [J.append(x) for x in C]
    return J
    
A = [3,8,2,5,1,4,7,6]
A = QuickSort(A)
print A
