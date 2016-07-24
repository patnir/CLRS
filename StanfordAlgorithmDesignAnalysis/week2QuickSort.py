# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 11:46:39 2016

@author: Rahul Patni
"""
import random

# quick sort implementation

# A : array to be sorted
# n : length of the array to be sorted

def ChoosePivot(A, left, right):
    #return random.randint(left, right)
    return int((left + right) / 2)

def QuickSortNoMem(A):
    if len(A) <= 1:
        return A
    p = ChoosePivot(A, 0, 0)
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
    pivot = ChoosePivot(A, left, right)
    Swap(A, pivot, left)
    while j <= right:
        if A[j] < A[left]:
            Swap(A, i, j)
            i += 1
        j += 1
    Swap(A, left, i - 1)
    print A
    QuickSort(A, left, i - 2)
    QuickSort(A, i, right)
    return
   
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return
    
#length = 10
#A = []
#[A.append(random.randint(0, 100)) for i in range(length)]
# A = [3, 8, 2, 5, 1, 4, 7, 6]
A = [1, 2, 3, 4, 5, 6]
print A
QuickSort(A, 0, len(A) - 1)
print A
