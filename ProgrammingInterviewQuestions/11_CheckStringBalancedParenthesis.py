# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:56:31 2016

@author: Rahul Patni
"""

# checking is string has balanced parenthesis

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None        
        
    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.size == 1:
            self.head = new_node
            return
        temp = self.head
        new_node.next = temp
        self.head = new_node
        return
        
    def printStack(self):
        if self.size == 0:
            return None
        temp = self.head
        while temp != None:
            print temp.value,
            temp = temp.next
        return
        
    def pop(self):
        if self.size == 0:
            return None
        ret_node = self.head
        self.head = self.head.next
        ret_node.next = None
        return ret_node
        


def checkBalanced(expression):
    return
    
def main():
    s = Stack()
    for i in range(0, 10):
        s.push(random.randint(0, 100))
    s.printStack()
    print
    print "pop"
    for i in range(0, s.size):
        ret = s.pop()
        print ret.value
    return
    
main()