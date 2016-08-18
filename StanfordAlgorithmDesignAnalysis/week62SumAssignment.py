# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:24:19 2016

@author: Rahul Patni
"""

# 2 SUM Week 6 Assignment
#import array

import random

def loadData():
    filename = "2sum.txt"
    fptr = open(filename)
    #A = array.array('l', range(1000000))
    A = []
    #i = 0
    for line in fptr:
        number = long(line.rstrip())
        A.append(number)
    return A
    
def ChoosePivot(A, left, right):
    #return random.randint(left, right)
    return int((left + right) / 2)

def QuickSort(A, left, right):
    if left >= right:
        return
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
    QuickSort(A, left, i - 2)
    QuickSort(A, i, right)
    return
   
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return

def TwoSum(A):
    total = 0
    for i in range(len(A) - 1):
        start = i
        end = start + 1
        diff = []
        if A[start] > 10000:
            break
        if A[start] == A[end]:
            continue
        t = abs(A[start] + A[end])
        while end < len(A) - 1:
            if t not in diff and t <= 10000:
                diff.append(t)
            end += 1
            t = abs(A[start] + A[end])
        total += len(diff)
    return total
    
def printArray(A):
    for i in range(5000, len(A)):
        print A[i],
        if i > 30:
            return

def testing():
#    A = []
#    for i in range(20):
#        A.append(random.randint(0, 20))
#    QuickSort(A, 0, len(A) - 1)
    A = [0, 1, 1, 1, 2, 2, 5, 5, 9, 10, 10, 10, 11, 11, 13, 13]# 12, 13, 13, 14, 15, 16, 16, 17, 18, 20, 20, 20]
    total = 0
    for i in range(len(A) - 1):
        print "for", A[i]
        start = i
        end = start + 1
        diff = []
        if A[start] >= 3:
            break
        if A[start] == A[end]:
            continue
        t = abs(A[start] + A[end])
        while end < len(A) - 1:
            if t not in diff and t < 3:
                diff.append(t)
                print "end", A[end]
            end += 1
            t = abs(A[start] + A[end])
        total += len(diff)
    print total

def main():
    A = loadData()
    print "load complete"
    QuickSort(A, 0, len(A) - 1)
    print "sort complete"
    print TwoSum(A)
    #print "now printing"
    #printArray(A)
    #testing()
    
    
if __name__ == "__main__":
    main()