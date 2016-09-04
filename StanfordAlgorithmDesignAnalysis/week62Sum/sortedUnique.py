# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 15:36:54 2016

@author: Rahul Patni
"""

# sorted unique

def loadData():
    filename = "sorted.txt"
    fptr = open(filename)
    A = []
    for line in fptr:
        line = line.rstrip()
        A.append(long(line))
    return A
    
def unique(A):
    filename = "uniqueSorted.txt"
    fptr = open(filename, "w")
    check = None
    for i in A:
        if i != check:
            fptr.write("{}\n".format(i))
            check = i
        
def main():
    A = loadData()
    print "data loaded"
    print len(A)
    unique(A)
    print "unique sorted"
    return
    
main()