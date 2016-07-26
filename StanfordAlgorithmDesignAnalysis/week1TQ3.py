# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:41:16 2016

@author: Rahul Patni
"""

# Theory Question 3 - Week 1

# You are given a sorted (from smallest to largest) array A of n distinct 
# integers which can be positive, negative, or zero. You want to decide whether 
# or not there is an index i such that A[i] = i. Design the fastest algorithm 
# that you can for solving this problem.

import random

def ChoosePivot(A, left, right):
    #return random.randint(left, right)
    median = int((left + right) / 2)
    medianValue = max(min(A[left],A[right]), min(max(A[left],A[right]),A[median]))

    if (medianValue == A[left]):
        return left
    if (medianValue == A[right]):
        return right
    return median
        
def QuickSort(A, left, right):
    if left >= right:
        return 0
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
    count = right - left
    count += QuickSort(A, left, i - 2)
    count += QuickSort(A, i, right)
    return count
   
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return       

def Merge(A, left, right):
    if right == left:
        if A[left] == left:
            return True, A[left], left
        return False, -1, -1
    i = int((right + left) / 2)
    if A[i] == i:
        return True, A[i], i
    if A[i] < i:
        return Merge(A, i + 1, right)
    return Merge(A, left, i - 1)
    
    
def RandomInitialization(n):
    A = []
    for i in range(n):
        A.append(random.randint(0, 10))
        
    A = []
    A = [-100, -50, -40, -20, 0, 1, 2, 3, 4, 9, 12, 14]
    return A
    
def main():
    A = RandomInitialization(15)
#    print A
#    QuickSort(A, 0, len(A) - 1)
    print A
    print Merge(A, 0, len(A) - 1)
    return
    
if __name__ == "__main__":
    main()