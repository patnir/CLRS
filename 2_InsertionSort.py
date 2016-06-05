# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 10:20:50 2016

@author: Rahul Patni
"""

def insertionSort(A):
    for j in range(1, len(A)):    
        key = A[j]
        # Insert A[j] into the sorted sequence A[1..j - 1]
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A
    


A = [31, 41, 59, 26, 41, 58]

A = insertionSort(A)

print A