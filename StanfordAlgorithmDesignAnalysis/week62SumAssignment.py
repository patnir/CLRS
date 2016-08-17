# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:24:19 2016

@author: Rahul Patni
"""

# 2 SUM Week 6 Assignment
#import array

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
        t = abs(A[start] - A[start + 1])
        while t <= 10000:
            total += 1
            start += 1
            if start == len(A) - 1:
                break
            t = abs(A[start] - A[start + 1])
    return total

def main():
    A = loadData()
    print "load complete"
    QuickSort(A, 0, len(A) - 1)
    print "sort complete"
    print TwoSum(A)
    
    
if __name__ == "__main__":
    main()