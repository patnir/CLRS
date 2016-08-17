# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:12:27 2016

@author: Rahul Patni
"""

# Week 6 Median Maintenance

import sys

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
        if self.size == 0:
            return None
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
        if self.size == 0:
            return None
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
    lowNumbers = HeapHigh()
    highNumbers = HeapLow()
    i = 0
    total = 0
    for line in fptr:
        number = int(line.rstrip())
        low = lowNumbers.extractMax()
        high = highNumbers.extractMin()
        if lowNumbers.size == 0 or number <= low:
            lowNumbers.insert(number)
        elif highNumbers.size == 0 or number >= high:
            highNumbers.insert(number)
        else:
            lowNumbers.insert(number)
        if low != None:
            lowNumbers.insert(low)
        if high != None:
            highNumbers.insert(high)
        median = 0
        if i != 0 and i % 2 == 0:
            if highNumbers.size < lowNumbers.size:
                highNumbers.insert(lowNumbers.extractMax())
            elif highNumbers.size > lowNumbers.size:
                lowNumbers.insert(highNumbers.extractMin())
            median = highNumbers.extractMin()
            print median
            highNumbers.insert(median)
        else:
            if lowNumbers.size > highNumbers.size:
                median = lowNumbers.extractMax()
                print median
                lowNumbers.insert(median)
            else:
                median = highNumbers.extractMin()
                print median
                highNumbers.insert(median)
        total += median
        i += 1
    print "outside", i
    print "low size", lowNumbers.size
    print "high size", highNumbers.size
    print total

class DynamicSortedArray():
    def __init__(self):
        self.size = 0
        self.data = []
    
    def insert(self, number):
        if self.size == 0:
            self.size += 1
            self.data.append(number)
            return
        middle = int(self.size / 2)
        while True:
            if self.data[middle] > number:
                middle += self.size + int((self.size - middle) / 2)
            return
        return

def medianMaintDynamicSortedArray():
    filename = "Median.txt"
    data = []
    fptr = open(filename)
    total = 0
    for line in fptr:
        data.append(int(line.rstrip()))
        data.sort()
        if len(data) % 2 == 0:
            index = len(data) / 2
            median = data[index - 1]
        else:
            index = (len(data) + 1) / 2
            median = data[index - 1]
        print median
        total += median
    print "total", total % 10000
    return

def main():
    medianMaintDynamicSortedArray()
    return
    
if __name__ == "__main__":
    main()