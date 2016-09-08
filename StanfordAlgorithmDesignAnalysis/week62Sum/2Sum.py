# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 15:43:12 2016

@author: Rahul Patni
"""

# 2 sum with unique sorted numbers

def loadData():
    A = []
    filename = "uniqueSorted.txt"
    fptr = open(filename)
    for line in fptr:
        A.append(long(line.rstrip()))
    return A
    
#def TwoSum(A):
#    total = 0
#    for i in range(len(A) - 1):
#        start = i
#        end = start + 1
#        diff = []
#        if A[start] > 10000:
#            break
#        if A[start] == A[end]:
#            continue
#        t = abs(A[start] + A[end])
#        while end < len(A) - 1:
#            if t not in diff and t <= 10000:
#                diff.append(t)
#            end += 1
#            t = abs(A[start] + A[end])
#        total += len(diff)
#    return total    
    
def binarySearch(A, number):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == number:
            return mid
        if A[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    
def TwoSum(A):
    numbersToCheck = range(-5, 6)
    total = 0
    for i in range(len(A)):
        #print i
        notFound = True
        j = 0
        while notFound and j < len(numbersToCheck):
            r = numbersToCheck[j]
            check = r - A[i]
            ret = binarySearch(A, check)
            if ret >= 0 and ret > i:
                print "found", A[i], A[ret]
                notFound = False
                total += 1
                nxt = ret + 1
                while nxt < len(A) and A[nxt] - A[i] in numbersToCheck:
                    total += 1
                    nxt += 1
            j += 1
    return total
    
def main():
    #A = loadData()
    #print len(A)    
    A = [-10, -5, -3, -2, 0, 5, 6]
    print TwoSum(A)
    
main()