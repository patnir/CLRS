# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 01:13:53 2016

@author: Rahul Patni
"""

# Randomized Selection Algorithm

import random

def choosePivot(A, left, right):
    median = int((left + right) * 0.5)
    medianValue = max(min(A[left], A[right]), min(max(A[left], A[right]), median))
    if medianValue == A[left]:
        return left
    if medianValue == A[right]:
        return right
    return median

def randomPivot(left, right):
    return random.randint(left, right)    
    
def quickSort(A, left, right):
    if left >= right:
        return
    pivot = choosePivot(A, left, right)
    i = left + 1
    j = left + 1
    swap(A, pivot, left)
    while i <= right:
        if A[i] < A[left]:
            swap(A, i, j)
            j += 1
        i += 1
    swap(A, left, j - 1)
    quickSort(A, left, j -  2)
    quickSort(A, j, right)
    return
    
def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp
    
# A is the array and i is the order statistic
def randomizedSelect(A, left, right, orderStat):
    if right == left:
        return A[right]
    pivot = randomPivot(left, right)
    i = left + 1
    j = left + 1
    swap(A, pivot, left)
    while i <= right:
        if A[i] < A[left]:
            swap(A, i, j)
            j += 1
        i += 1
    swap(A, left, j - 1)
    if orderStat == (j - 1):
        return A[j - 1]
    if orderStat > (j - 1):
        return randomizedSelect(A, j, right, orderStat)
    return randomizedSelect(A, left, j - 2, orderStat)
    
length = 10
A = []
[A.append(random.randint(0, 100)) for i in range(length)] 
    
print A
print
print randomizedSelect(A, 0, len(A) - 1, 0)
quickSort(A, 0, len(A) - 1)
print A