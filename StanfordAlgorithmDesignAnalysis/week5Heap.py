# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:48:31 2016

@author: Rahul Patni
"""

# heap data structure

class Heap():
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
            print "loop though"
            check2 = int(check / 2.0)
            if self.data[check - 1] < self.data[check2 - 1]:
                print "print called"
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
        
def main():
    heap = Heap()
    array = [13, 11, 9, 12, 4, 9, 8, 4, 4, 9, 15, 1, -7, -9, -123, 10]
    for i in array:
        heap.insert(i)
        print "printing heap for", i
        heap.printData()
    print "extracting"
    while heap.size > 0:
        print heap.extractMin()
    return
    
if __name__ == "__main__":
    main()
        