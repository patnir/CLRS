# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:32:08 2016

@author: Rahul Patni
"""

#quick and merge sort
import random

def partition(A, start, end):
    pivot = A[start]
    down = start
    up = end
    while down < up:
        while A[down] <= pivot and down < end:
            down += 1
        while A[up] > pivot:
            up -= 1
        if down < up:
            A[down], A[up] = A[up], A[down]
    A[start] = A[up]
    A[up] = pivot
    return up
    

def Quicksort(A, start, end):
    if start >= end:
        return
    index = partition(A, start, end)
    Quicksort(A, start, index - 1)
    Quicksort(A, index + 1, end)
    return
    
def merge(A, start, mid, end):
    B = [0] * (mid - start + 1)
    C = [0] * (end - mid)
    bLength = mid - start + 1
    cLength = end - mid
    for i in range(0, bLength):
        B[i] = A[start + i]
    for i in range(0, cLength):
        C[i] = A[start + bLength + i]
    print "printing arrays", start, end, mid
    print B
    print C
    print A
    
    j = 0
    k = 0
    for i in range(start, end + 1):
        if k >= cLength or (j < bLength and B[j] < C[k]):
            A[i] = B[j]
            j += 1
        else:
            A[i] = C[k]
            k += 1
    print A
    return    
    
def MergeSort(A, start, end):
    if start >= end:
        return
    mid = (start + end) / 2
    MergeSort(A, start, mid)
    MergeSort(A, mid + 1, end)
    merge(A, start, mid, end)
    return
    
def newMergeSort(A, start, end):
    if start >= end:
        return
    mid = (start + end) / 2
    newMergeSort(A, start, mid)
    newMergeSort(A, mid + 1, end)
    newMerge(A, start, mid, end)
    return

def newMerge(A, start, mid, end):
    temp = [0] * (end - start + 1)
    for i in range(start, end + 1):
        temp[i] = A[i]
    i = start
    j = mid + 1
    for k in range(start, end + 1):
        if (i > mid):
            A[k] = temp[j]
            j += 1
        elif (j > end):
            A[k] = temp[i]
            i+= 1
        
    return    

def main():
    size = 10
    A = [0]* size
    for i in range(size):
        A[i] = random.randint(10, 20)
    print A
    B = list(A)
    C = list(A)
    B.sort()
    print B
    
    newMergeSort(C, 0, len(C) - 1)
    print "after merge sort"

    print C
    print "after quick sort"
    Quicksort(A, 0, len(A) - 1)
    print A    
    return
    
    
main()