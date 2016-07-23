# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 11:46:39 2016

@author: Rahul Patni
"""

# quick sort implementation

# A : array to be sorted
# n : length of the array to be sorted

def ChoosePivot(A, n):
    # For now, returning 1
    return 0

def QuickSort(A, n):
    p = ChoosePivot(A, n)
    J = []
    print A
    for i in A:
        if i < A[p]:
            J.append(i)
    J.append(A[p])
    for i in A:
        if i > A[p]:
            J.append(i)
    print J
#    B = []    
#    C = []
#    QuickSort(B, 1)
#    QuickSort(C, 1)
    return
    
A = [3,8,2,5,1,4,7,6]
QuickSort(A, len(A))