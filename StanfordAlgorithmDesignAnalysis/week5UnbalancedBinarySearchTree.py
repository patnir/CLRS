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
        return 
        
    def preOrder(self):
        return
        
    def inOrder(self):
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
            print self.root.postOrder()
        return
        
    def preOrder(self):
        return
        
    def inOrder(self):
        return
        

        