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

def modifiedBinarySearch(A, target, start, end):
    if target < A[start]:
        return start
    if target > A[end]:
        return end
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        if A[mid] > target and A[mid - 1] < target:
            return mid
        if A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def modifiedBinarySearch2(A, target, start, end):
    if target < A[start]:
        return start
    if target > A[end]:
        return end
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        if A[mid] < target and A[mid + 1] > target:
            return mid
        if A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def test(A):
    highRange = 10
    lowRange = -10
    i = 0
    total = 0
    while i < len(A) and A[i] < 10:
        j = modifiedBinarySearch(A, highRange - A[i], i, len(A) - 1)
        k = modifiedBinarySearch2(A, lowRange - A[i], i, len(A) - 1)
        print "i", i, "j", j, "k", k
        print A[i], A[j], A[k]
        i += 1
        total += j - i
        print total
    print A
    
def main():
    A = []
    for i in range(10):
        A.append(random.randint(-50, 50))
    A.sort()
    A = [-45, -41, -33, -29, -18, 16, 23, 23, 24, 38, 54]
    test(A)
    
main()