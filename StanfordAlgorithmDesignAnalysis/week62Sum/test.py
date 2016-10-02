# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 15:32:49 2016

@author: Rahul Patni
"""

# test

'''

def loadData():
    A = []
    filename = "uniqueSorted.txt"
    fptr = open(filename)
    for line in fptr:
        A.append(long(line.rstrip()))
    return A
    
    
    
def main():
    A = loadData()
    print A
    
main()

'''

import random

def binarySearch(A, target, start, end):
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        if A[mid] > target and A[mid - 1] < target:
            return mid
        if A[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    return - 1

def test(A):
    lowRange = -10
    highRange = 10
    for i in A:
        return
    print A
    
def main():
    A = []
    for i in range(10):
        A.append(random.randint(-50, 50))
    A.sort()
    A = [-45, -41, -33, -29, -18, 16, 23, 23, 24, 38]
    test(A)
    
main()