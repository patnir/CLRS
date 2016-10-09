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
        while val > parent and parentIndex > 0:
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
            if self.array[parentIndex - 1] < self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def extractMax(self):
        if self.end == 0:
            return None
            
        toRemove = self.array[0]
        
        self.end -= 1
        self.array[0] = self.array[self.end]
        self.array[self.end] = None
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.end:
        #while child1Index <= self.end and (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
            if child2Index > self.end:
                child2Index = child1Index
            if (self.array[currIndex - 1] < self.array[child1Index - 1] or self.array[currIndex - 1] < self.array[child2Index - 1]):
                if self.array[child1Index - 1] >= self.array[child2Index - 1]:
                    self.array[child1Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child1Index - 1] 
                    currIndex = child1Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
                else:
                    self.array[child2Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child2Index - 1] 
                    currIndex = child2Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
            else:
                child1Index = self.end + 1
        
        self.checkHeapProperty()
        return toRemove
        

def main():
    h = Heap()
    for i in range(20):
        val = random.randint(10, 90)
        print val
        h.insert(val)
        print h.array
        h.checkHeapProperty()
    
    print h.array
    
    while h.end != 0:
        val = h.extractMax()
        print val
        print h.array
    
main()