# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:01:21 2016

@author: Rahul Patni
"""

# Week 1 Programming Assignment Solution

def Merge(A, p, r):
    x = y = z = 0
    if p < r:
        q = int((p + r) / 2)
        x = Merge(A, p, q)
        y = Merge(A, q + 1, r)
        z = MergeSort(A, p, q, r)
    return x + y + z
    
def MergeSort(A, p, q, r):
    n1 = range(p, q + 1)
    n2 = range(q + 1, r + 1)
    B = []
    C = []
    for i in n1:
        B.append(A[i])
    for i in n2:
        C.append(A[i])
    i = 0
    j = 0
    inversions = 0
    for k in range(p, r + 1):
        if j == len(C) or (i < len(B) and B[i] <= C[j]):
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j] 
            j += 1
            inversions += len(range(i, len(B)))
    return inversions

def loadData(array):
    filename = "IntegerArray.txt"
    fhand = open(filename)
    for line in fhand:
        array.append(int(line.rstrip()))
    
def main():
    X = []
    loadData(X)
    print Merge(X, 0, len(X) - 1)
    

if __name__ == "__main__":
    main()