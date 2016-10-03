# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 21:24:40 2016

@author: Rahul Patni
"""

# heap sort

import random

class Heap():
    def __init__(self):
        self.array = [0] * 30
        self.start = 0
        self.end = 0
        
    def insert(self, val):
        self.array[self.end] = val
        currIndex = self.end + 1
        parentIndex = currIndex / 2
        #print "out", currIndex, parentIndex
        parent = self.array[parentIndex - 1]
        #print val, parent
        while val < parent and parentIndex > 0:
            #print "parent", "child", parentIndex - 1, currIndex - 1
            #print self.array[parentIndex - 1], self.array[currIndex - 1]
            self.array[parentIndex - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[parentIndex - 1]
            currIndex = parentIndex
            parentIndex = currIndex / 2
            parent = self.array[parentIndex - 1]
        self.end += 1
        return
        
    def checkHeapProperty(self):
        print "end", self.end
        currIndex = self.end
        parentIndex = currIndex / 2
        while parentIndex > 0:
            if self.array[parentIndex - 1] > self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def extractMin(self):
        return
        
    def printHeap(self):
        print self.array
        
        
def main():
    heap = Heap()
    for i in range(20):
        val = random.randint(10, 90)
        heap.insert(val)
        heap.printHeap()
        heap.checkHeapProperty()
        
main()