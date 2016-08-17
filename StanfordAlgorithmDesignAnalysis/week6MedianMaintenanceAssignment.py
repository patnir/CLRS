# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:12:27 2016

@author: Rahul Patni
"""

# Week 6 Median Maintenance

class HeapLow():
    def __init__(self):
        self.size = 0
        self.data = []
    
    def insert(self, number):
        self.data.append(number)
        self.size += 1
        if self.size == 1:
            return
        # case if not added to correct position
        check = self.size
        while check > 1:
            check2 = int(check / 2.0)
            if self.data[check - 1] < self.data[check2 - 1]:
                self.swap(check - 1, check2 - 1)
            check = check2
        return

    def swap(self, a, b):
        temp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = temp
        
    def printData(self):
        for i in self.data:
            print i
        
    def extractMin(self):
        self.size -= 1
        toReturn = self.data[0]
        self.data[0] = self.data[self.size]
        self.data.pop()
        # to correct the tree
        check = 1
        left = 2 * check
        right = left + 1
        while left <= self.size:
            if right > self.size:
                right = left
            toSwap = left
            if self.data[left - 1] > self.data[right - 1]:
                toSwap = right
            if self.data[check - 1] > self.data[toSwap - 1]:
                self.swap(check - 1, toSwap - 1)
            check = toSwap
            left = toSwap * 2
            right = left + 1
        return toReturn
        
        
class HeapHigh():
    def __init__(self):
        self.size = 0
        self.data = []
    
    def insert(self, number):
        self.data.append(number)
        self.size += 1
        if self.size == 1:
            return
        # case if not added to correct position
        child = self.size
        while child > 1:
            parent = int(child / 2.0)
            if self.data[child - 1] >= self.data[parent - 1]:
                self.swap(parent - 1, child - 1)
            child = parent
        return

    def swap(self, a, b):
        temp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = temp
        
    def printData(self):
        for i in self.data:
            print i
        
    def extractMax(self):
        self.size -= 1
        toReturn = self.data[0]
        self.data[0] = self.data[self.size]
        self.data.pop()
        # to correct the tree
        parent = 1
        left = 2 * parent
        right = left + 1
        while left <= self.size:
            if right > self.size:
                right = left
            toSwap = right
            if self.data[left - 1] > self.data[right - 1]:
                toSwap = left
            if self.data[parent - 1] < self.data[toSwap - 1]:
                self.swap(parent - 1, toSwap - 1)
            parent = toSwap
            left = toSwap * 2
            right = left + 1
        return toReturn
        
def medianMaintenance():
    filename = "Median.txt"
    fptr = open(filename)
    low = HeapLow()
    high = HeapHigh()
    for line in fptr:
        number = int(line.rstrip())
        low.insert(number)
        high.insert(number)
        lowest = low.extractMin()
        print "lowest", lowest
        highest = high.extractMax()
        print "highest", highest
        low.insert(lowest)
        high.insert(highest)

def main():
    medianMaintenance()
    return
    
if __name__ == "__main__":
    main()