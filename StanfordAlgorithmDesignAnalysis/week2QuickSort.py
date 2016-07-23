# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 11:46:39 2016

@author: Rahul Patni
"""
import random

# quick sort implementation

# A : array to be sorted
# n : length of the array to be sorted

def ChoosePivot(A):
    # For now, returning 1
    return 0

def QuickSortNoMem(A):
    if len(A) <= 1:
        return A
    p = ChoosePivot(A)
    B = []
    C = []
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

def QuickSort(A, left, right):
    if left >= right:
        return
    i = left + 1
    j = left + 1
    pivot = A[left]
    while j <= right:
        if A[j] < pivot:
            Swap(A, i, j)
            i += 1
        j += 1
    print A
    Swap(A, left, i - 1)
    QuickSort(A, left, i - 2)
    QuickSort(A, i, right)
    return
   
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return
    
length = 10
A = []
[A.append(random.randint(0, 100)) for i in range(length)]
# A = [3, 8, 2, 5, 1, 4, 7, 6]
print A
QuickSort(A, 0, len(A) - 1)
print A
