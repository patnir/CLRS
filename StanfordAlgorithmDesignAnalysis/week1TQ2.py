# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:08:54 2016

@author: Rahul Patni
"""

# week1TQ2

# You are a given a unimodal array of n distinct elements, meaning that its 
# entries are in increasing order up until its maximum element, after which its 
# elements are in decreasing order. Give an algorithm to compute the maximum 
# element that runs in O(log n) time.

def Merge(A):
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        if A[0] > A[1]:
            return A[0]
        return A[1]
    i = int(len(A) / 2)
    j = int(len(A) / 2) + 1
    if A[i] > A[j]:
        B = []
        for k in range(0, i + 1):
            B.append(A[k])
        return Merge(B)
    C = [] 
    for k in range(j, len(A)):
        C.append(A[k])
    return Merge(C)
    
def getInput(n):
    A = []
    #n = int(raw_input("Enter a positive integer"))
    for i in range(n):
        A.append(i + 1)
    for i in reversed(range(n)):
        A.append(i)
    print A
    return A
    
def main():
    A = getInput(200)
    print Merge(A)
    
if __name__ == "__main__":
    main()