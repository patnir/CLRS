# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 09:19:50 2016

@author: Rahul Patni
"""

# Circular array search

def circularArraySearch(A, target):
    start = 0
    end = len(A) - 1
    while start <= end:
        high = A[start]
        low = A[end]
        firstHalf = True if A[start] <= target else False
        print start, end, firstHalf
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        if high <= low:
            if A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        elif (firstHalf and (A[mid] >= target or A[mid] <= high)) or ((firstHalf == False) and A[mid] >= target):
            print "here 1"
            end = mid - 1
        else:
            print "here 2"
            start = mid + 1
    return False
    
def main():
    A = [12, 13, 15, 16, 17, 1, 2, 3, 4, 5, 6, 7]
    print circularArraySearch(A, 7)
    return
    
    
main()