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
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.end:
        #while child1Index <= self.end and (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
            if child2Index > self.end:
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
                child1Index = self.end + 1
        return toRemove
        
    def isEmpty(self):
        return self.end == 0     
        
        
    def delete(self, target):
        if self.isEmpty == True:
            print "Empty array"
            return None
        i = 0
        while i < self.end and target != self.array[i]:
            i += 1    
        if self.array[i] == None:
            print "Not found"
            return None    
        print target, "found at", i
        
        self.end -= 1
        self.array[i] = self.array[self.end]
        self.array[self.end] = None        
        
        '''
        currIndex = i + 1
        child1Index = currIndex * 2
        child2Index = child1Index + 1
        '''
        
        curr = i + 1
        child1 = curr * 2
        child2 = child1 + 1
        
        if child2 > self.end:
                child2 = child1        
        
        while (child1 <= self.end and self.array[child1 - 1] < self.array[curr - 1]) or (child2 <= self.end and self.array[child2 - 1] < self.array[curr - 1]):
            if self.array[child1 - 1] <= self.array[child2 - 1]:
                self.array[curr - 1], self.array[child1 - 1] = self.array[child1 - 1], self.array[curr - 1]
                curr = child1                
            else:
                self.array[curr - 1], self.array[child2 - 1] = self.array[child2 - 1], self.array[curr - 1]
                curr = child2
            
            child1 = curr * 2
            child2 = child1 + 1
            
            if child2 > self.end:
                child2 = child1
        '''        
        while child1Index <= self.end:
            
            if child2Index > self.end:
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
                child1Index = self.end + 1'''
        return
            
       
       
        
def main():
    heap = Heap()

    s = []    
    
    for i in range(20):
        val = random.randint(40, 90)
        s.append(val)
        heap.insert(val)
        heap.checkHeapProperty()

    print heap.array    
    print "extracting"
    
    for i in s:
        heap.delete(i)
        print heap.array
        heap.checkHeapProperty()
    
    '''while heap.isEmpty() != True:
        val = heap.extractMin()
        print val'''
        
main()
    