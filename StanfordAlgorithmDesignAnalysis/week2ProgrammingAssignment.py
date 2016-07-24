# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 00:34:32 2016

@author: Rahul Patni
"""

# Assignment solution

A = []

def loadData():
    filename = "QuickSort.txt"
    fhand = open(filename)
    for line in fhand:
        A.append(int(line.rstrip()))
    
def ChoosePivot(A, left, right):
    #return random.randint(left, right)
    median = int((left + right) / 2)
    medianValue = max(min(A[left],A[right]), min(max(A[left],A[right]),A[median]))

    if (medianValue == A[left]):
        return left
    if (medianValue == A[right]):
        return right
    return median
        
def QuickSort(A, left, right):
    if left >= right:
        return 0
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
    count = right - left
    count += QuickSort(A, left, i - 2)
    count += QuickSort(A, i, right)
    return count
   
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return        
        
def main():
    loadData()
    count = QuickSort(A, 0, len(A) - 1)
    print A
    print count
    
if __name__ == "__main__":
    main()