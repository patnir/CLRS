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
        self.size = 0
        
    def insert(self, val):
        self.array[self.size] = val
        self.size += 1
        currIndex = self.size
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
        currIndex = self.size
        parentIndex = currIndex / 2
        while parentIndex > 0:
            if self.array[parentIndex - 1] > self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def newInsert(self, val):
        self.array[self.size] = val
        self.upwardHeapify(self.size)        
        self.size += 1
        
    def upwardHeapify(self, index):
        temp = self.array[index]
        parent = (index + 1) / 2 - 1
        child = index
        while parent >= 0 and self.array[parent] > temp:
            self.array[child] = self.array[parent]
            child = parent
            parent = (parent + 1) / 2 - 1
        self.array[child] = temp
        return
     
    def downwardHeapify(self, index):
        temp = self.array[index]
        notOrdered = True
        parent = index
        while notOrdered and parent < self.size / 2:
            child = (parent + 1) * 2 - 1
            if child < self.size - 1 and self.array[child] > self.array[child + 1]:
                child += 1
            if temp <= self.array[child]:
                notOrdered = False
            else:
                self.array[parent] = self.array[child]
                parent = child
        self.array[parent] = temp
        return
        
    def newExtractMin(self):
        if self.size == 0:
            return None
        toRemove = self.array[0]
        self.size -= 1
        self.array[0] = self.array[self.size]
        self.array[self.size] = None
        self.downwardHeapify(0)
        return toRemove
         
    def extractMin(self):
        if self.size == 0:
            return None
            
        toRemove = self.array[0]
        
        self.size -= 1
        self.array[0] = self.array[self.size]
        self.array[self.size] = None
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.size:
        #while child1Index <= self.size and (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
            if child2Index > self.size:
                child2Index = child1Index
            if (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
                if self.array[child1Index - 1] <= self.array[child2Index - 1]:
                    self.array[child1Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child1Index - 1] 
                    currIndex = child1Index
                    
                else:
                    self.array[child2Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child2Index - 1] 
                    currIndex = child2Index
                    
                child1Index = currIndex * 2
                child2Index = currIndex * 2 + 1
            else:
                child1Index = self.size + 1
        return toRemove
        
    def isEmpty(self):
        return self.size == 0     
        
        
    def delete(self, target):
        if self.isEmpty == True:
            print "Empty array"
            return None
        i = 0
        while i < self.size and target != self.array[i]:
            i += 1    
        if self.array[i] == None:
            print "Not found"
            return None    
        print target, "found at", i
        
        self.size -= 1
        self.array[i] = self.array[self.size]
        self.array[self.size] = None        
        
        '''
        currIndex = i + 1
        child1Index = currIndex * 2
        child2Index = child1Index + 1
        '''
        
        curr = i + 1
        child1 = curr * 2
        child2 = child1 + 1
        
        if child2 > self.size:
                child2 = child1        
        
        while (child1 <= self.size and self.array[child1 - 1] < self.array[curr - 1]) or (child2 <= self.size and self.array[child2 - 1] < self.array[curr - 1]):
            if self.array[child1 - 1] <= self.array[child2 - 1]:
                self.array[curr - 1], self.array[child1 - 1] = self.array[child1 - 1], self.array[curr - 1]
                curr = child1                
            else:
                self.array[curr - 1], self.array[child2 - 1] = self.array[child2 - 1], self.array[curr - 1]
                curr = child2
            
            child1 = curr * 2
            child2 = child1 + 1
            
            if child2 > self.size:
                child2 = child1
        '''        
        while child1Index <= self.size:
            
            if child2Index > self.size:
                child2Index = child1Index
                
            if (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
                if self.array[child1Index - 1] <= self.array[child2Index - 1]:
                    self.array[child1Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child1Index - 1] 
                    currIndex = child1Index
                    
                else:
                    self.array[child2Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child2Index - 1] 
                    currIndex = child2Index
                    
                child1Index = currIndex * 2
                child2Index = currIndex * 2 + 1
            else:
                child1Index = self.size + 1'''
        return
            
       
       
        
def main():
    heap = Heap()

    s = []    
    
    for i in range(20):
        val = random.randint(40, 90)
        s.append(val)
        heap.newInsert(val)
        heap.checkHeapProperty()

    print heap.array    
    print "extracting"
    
    for i in s:
        val = heap.newExtractMin()
        print "minimum value", val
        print heap.array
        heap.checkHeapProperty()
    
    '''while heap.isEmpty() != True:
        val = heap.extractMin()
        print val'''
        
main()
    