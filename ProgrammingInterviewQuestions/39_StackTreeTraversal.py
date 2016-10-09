# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 16:56:30 2016

@author: Rahul Patni
"""

# tree traversal stack inorder

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (thevalue of the node)
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.n = None

class Stack():
    def __init__(self):
        self.head = None
    
    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            return 
        node.n = self.head
        self.head = node
        return
    
    def pop(self):# -*- coding: utf-8 -*-
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
        print self.data,
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
        self.total = 0
        
    def push(self, tree):
        self.total += 1
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
        self.total -= 1
        return toRet.tree
        
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
    if root == None:
        return
    s = Stack()
    curr = root
    while curr != None or s.isEmpty() == False:
        while curr != None:
            s.push(curr)
            curr = curr.left
        n = s.pop()
        print n.data,
        curr = n.right
    print
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
    
def depthFirstWithStack(root):
    if root == None:
        return
    s = Stack()
    s.push(root)
    
    while s.isEmpty() == False:
        curr = s.pop()
        print curr.data,
        if curr.right != None:
            s.push(curr.right)
        if curr.left != None:
            s.push(curr.left)
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
    print
    stackInorder(root)

    depthFirst(root)
    depthFirstWithStack(root)

main()
        
        if self.head == None:
            return Node
        toRet = self.head
        self.head = self.head.n
        toRet.n = None
        return toRet
    
    def stackTop(self):
        if self.head == None:
            return None
        node = Node(self.head.val)
        return node
        
            

def inOrder(root):
    #Write your code here
    curr = Node(root, root.data)
     
    stack = Stack()
    
    print stack.stackTop()
    
    stack.push(curr)
    while stack.stackTop() == None:
        return
        
    
