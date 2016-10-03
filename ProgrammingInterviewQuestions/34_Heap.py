# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 21:24:40 2016

@author: Rahul Patni
"""

# heap sort

import random

class Heap():
    def __init__(self):
        self.array = [None] * 30
        self.start = 0
        self.end = 0
        
    def insert(self, val):
        self.array[self.end] = val
        self.end += 1
        currIndex = self.end
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
        return
        
    def checkHeapProperty(self):
        currIndex = self.end
        parentIndex = currIndex / 2
        while parentIndex > 0:
            if self.array[parentIndex - 1] > self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def extractMin(self):
        if self.end == 0:
            return None
        toRemove = self.array[0]
        self.end -= 1
        self.array[0] = self.array[self.end]
        self.array[self.end] = None
        
        self.printHeap()
        
        return toRemove
        
    def printHeap(self):
        print self.array
        
        
def main():
    heap = Heap()
    for i in range(20):
        val = random.randint(10, 90)
        heap.insert(val)
        heap.printHeap()
        heap.checkHeapProperty()
    heap.extractMin()
        
main()