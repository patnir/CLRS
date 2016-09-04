# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 15:25:49 2016

@author: Rahul Patni
"""

# 2 sum

def loadData():
    filename = "2sum.txt"
    fptr = open(filename)
    #A = array.array('l', range(1000000))
    A = []
    #i = 0
    for line in fptr:
        number = long(line.rstrip())
        A.append(number)
    fptr.close()
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
    
def checkSort(A):
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            print "sort failed"
            return False
        print "sort succeeded"
        return True
    
def writeData(A):
    filename = "sorted.txt"
    fptr = open(filename, "w")
    for i in A:
        fptr.write("{}\n".format(i))
    fptr.close()
    print "written to file"
    return    
    
def main():
    A = loadData()
    print "load complete"
    QuickSort(A, 0, len(A) - 1)
    print "sort complete"
    print checkSort(A)
    writeData(A)
    
main()