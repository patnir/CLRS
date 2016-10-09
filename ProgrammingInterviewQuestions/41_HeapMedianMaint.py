# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 17:32:29 2016

@author: Rahul Patni
"""

# heap median maintenance

class HeapMin():
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

class HeapMax():
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
    

def medianMaint(n):
    heapMin = HeapMin()
    heapMax = HeapMax()
    for i in range(0, n):
        val = map(int, raw_input().strip().split(' '))
        val = val[0]
        
        if heapMax.end == 0:
            heapMax.insert(val)
            print val / 1.0
        elif heapMin.end == 0:
            maxp = heapMax.extractMax()
            if maxp > val:
                heapMin.insert(maxp)
                heapMax.insert(val)
            else:
                heapMin.insert(val)
                heapMax.insert(maxp)
            print (maxp + val) / 2.0
        else:
            if val <= heapMax.array[0]:
                heapMax.insert(val)
            else:
                heapMin.insert(val)
            if heapMax.end >= heapMin.end + 2:
                maxp = heapMax.extractMax()
                heapMin.insert(maxp)
            elif heapMin.end >= heapMax.end + 2:
                minp = heapMin.extractMin()
                heapMax.insert(minp)
            if (heapMax.end + heapMin.end) % 2 == 0:
                maxp = heapMin.array[0]
                minp = heapMax.array[0]
                mid = (maxp + minp) / 2.0
            else:
                if heapMax.end > heapMax.end:
                    mid = heapMax.array[0] / 1.0
                else:
                    mid = heapMin.array[0] / 1.0
                    
            print mid
            
        

def main():
    n = int(raw_input().strip())
    
    medianMaint(n)
        
    
    
main()


