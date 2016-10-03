# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 18:52:48 2016

@author: Rahul Patni
"""

# Reduction Cost

# heap sort

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
        parent = self.array[parentIndex - 1]
        
        while val < parent and parentIndex > 0:
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
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.end:
            if child2Index > self.end:
                child2Index = child1Index
            if (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
                if self.array[child1Index - 1] <= self.array[child2Index - 1]:
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
        
        return toRemove
        
    def printHeap(self):
        print self.array
 

# O(n log(n)) implementation using a headp:

def reductionCost(A):
    heap = Heap()
    
    # Following for loop takes O(n log(n)) time    
    for i in A:
        heap.insert(i) # O(log(n))

    cost = 0
    heap.printHeap()

    # Following for loop takes O(n log(n)) time    
    
    while heap.end > 1:
        heap.printHeap()
        first = heap.extractMin() # O(log(n))
        second = heap.extractMin() # O(log(n))
        heap.insert(first + second) # O(log(n))
        cost += first + second
    return cost   
        
def main():
    A =  [4, 3, 2, 1]
    print reductionCost(A)
        
main()