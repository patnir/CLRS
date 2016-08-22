# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:56:39 2016

@author: Rahul Patni
"""

# Reverse a linked list

import random

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        
    def printForward(self):
        if self.next == None:
            print self.value, 
            return
        print self.value, 
        self.next.printForward()
        
class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
            
    def push(self, val):
        node = Node(val)
        self.size += 1
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head = node
    
    def pop(self):
        toReturn = None
        if self.head == None:
            return toReturn
        toReturn = self.head
        self.head= self.head.next
        toReturn.next = None
        self.size -= 1
        return toReturn
        
    def printForward(self):
        if self.head == None:
            return
        self.head.printForward()
        return
        
    def reverse(self):
        if self.head == None:
            return
        curr = self.head.next
        prev = self.head
        temp = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            if prev == self.head:
                prev.next = None
            prev = curr
            curr = temp
        self.head = prev
        return
    
def main():
    l = LinkedList()
    for i in range(0):
        val = random.randint(10, 50)
        l.push(val)
    l.printForward()
    l.reverse()
    print
    l.printForward()
    
    return
    
main()