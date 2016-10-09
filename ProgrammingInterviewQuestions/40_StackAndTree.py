# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 19:41:47 2016

@author: Rahul Patni
"""

# Stack and Tree

import random

# changing to stack for tree

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def Inorder(self):
        if self.left != None:
            self.left.Inorder()
        print self.data
        if self.right != None:
            self.right.Inorder()
        return

class StackNode():
    def __init__(self, tree = Node(0)):
        self.tree = tree
        self.next = None
        
    def printTree(self):
        print self.tree
        return

class Stack():
    def __init__(self):
        self.head = None
        
    def push(self, tree):
        node = StackNode(tree)
        
        if self.head == None:
            self.head = node
            return
            
        node.next = self.head
        self.head = node
        return
        
    def pop(self):
        if self.head == None:
            return None
        toRet = self.head
        self.head = self.head.next
        toRet.next = None
        
        return toRet
        
    def printStack(self):
        if self.head == None:
            return
        curr = self.head
        while curr != None:
            print str(curr.printTree()) + "->",
            curr = curr.next
            
        print
        
        return
        
    def isEmpty(self):
        if self.head == None:
            return True
        return False
 

def stackInorder(root):
    
    return
    
    
def breadthFirst(root):
    return
    
    
def depthFirst(root):
    if root == None:
        return
    s = []
    s.append(root)
    while len(s) != 0:
        curr = s.pop()
        print curr.data, 
        if curr.right != None:
            s.append(curr.right)
        if curr.left != None:
            s.append(curr.left)
    print
    return
       
def main():
    '''
    for i in range(20):
        val = random.randint(-200, 200)
        print val
        stack.push(val)
        
    stack.printStack()
    
    while stack.isEmpty() == False:
        ret = stack.pop()
        print ret.val
        stack.printStack()
    stack.printStack()    '''
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    root.right.left = Node(8)
    root.Inorder()
        
    depthFirst(root)

main()
        