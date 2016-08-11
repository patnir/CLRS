# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 06:04:03 2016

@author: Rahul Patni
"""

# Unbalanced Binary Search Tree

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
    def insert(self, val):
        if val <= self.value:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        
    def search(self, val):
        if val == self.value:
            return True
        if val < self.value:
            if self.left == None:
                return False
            else:
                return self.left.search(val)
        else:
            if self.right == None:
                return False
            else:
                return self.right.search(val)
        return
        
    def postOrder(self):
        if self == None:
            return
        self.left.postOrder()
        self.right.postOrder()
        print self.value,
        return 
        
    def preOrder(self):
        if self == None:
            return
        print self.value,
        self.left.preOrder()
        self.right.preOrder()
        return
        
    def inOrder(self):
        if self == None:
            return
        self.left.inOrder()
        print self.value, 
        self.right.inOrder()
        return

class BST():
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root != None:
            self.root.insert(val)
            return
        else:
            self.root = Node(val)
        return
        
    def search(self, val):
        if self.root == None:
            return False
        return self.root.search(val)
        
    def postOrder(self):
        if self.root == None:
            return None
        else:
            self.root.postOrder()
        return
        
    def preOrder(self):
        if self.root == None:
            return None
        else:
            self.root.preOrder()
        return
        
    def inOrder(self):
        if self.root == None:
            return None
        else:
            self.root.inOrder()
        return
        
        
        
        

        