# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 18:45:32 2016

@author: Rahul Patni
"""

# selection sort

import random

def selectionSort(A):
    for i in range(len(A) - 1, 0, -1):
        mI = 0
        for j in range(1, i + 1):
            if A[j] >= A[mI]:
                mI = j
        A[i] = A[mI]
        
    print A
    
    checkIncreasing(A)
    return
    

def checkIncreasing(A):
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            print "not increasing"
            return
    print "increasing"
    return     
    
def main():
    A = []    
    for i in range(101):
        A.append(random.randint(10, 90))
    print A
    selectionSort(A)
    
    
main()