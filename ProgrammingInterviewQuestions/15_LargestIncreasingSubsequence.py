# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:47:20 2016

@author: Rahul Patni
"""

# largest increasing sub sequence

def lis(A):
    total = 0
    for i in range(0, len(A)):
        largest = A[i]
        currTotal = 1
        for j in range(i + 1, len(A)):
            if A[j] > largest:
                largest = A[j]
                currTotal += 1
        if currTotal > total:
            total = currTotal
        return total

def main():
    A = [5,6,7,8,9,10,11,12,13,1,2,3,4,8,9,2,10,11,14,15]
    print lis(A)
    return
    
main()