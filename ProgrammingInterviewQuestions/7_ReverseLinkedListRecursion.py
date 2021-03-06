# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:23:45 2016

@author: Rahul Patni
"""

# Reverse a linked list with recursion

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
    
    def reverse(self):
        if self.next == None:
            return self
        self.next = self.reverse()
        
        
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
        
def reverse(head):
    if head.next == None:
        return head
    new_head = reverse(head.next)
    ret = new_head
    while ret.next != None:
        ret = ret.next
        print ret.value
    ret.next = head
    return new_head
        
def main():
    l = LinkedList()
    for i in range(10):
        val = random.randint(10, 50)
        l.push(val)
    l.printForward()
    l.head = reverse(l.head)
    print
    l.printForward()
    return
    
main()