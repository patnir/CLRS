# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 21:00:45 2016

@author: Rahul Patni
"""

# modifies binary

def modifiedBinarySearch(A, target, start, end):
    if target < A[start]:
        return start
    if target > A[end]:
        return end
    while start <= end:
        mid = (start + end) / 2
        print A[mid]
        if A[mid] == target:
            return mid
        if A[mid] > target and A[mid - 1] < target:
            return mid
        if A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
    
    
def main():
    A = [1, 2, 3, 4, 11]
    print modifiedBinarySearch(A, 15, 0, len(A) - 1)
    
    
main()