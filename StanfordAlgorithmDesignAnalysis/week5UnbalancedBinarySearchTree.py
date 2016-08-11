# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 06:04:03 2016

@author: Rahul Patni
"""
import random

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
        if self.left != None:
            self.left.postOrder()
        if self.right != None:
            self.right.postOrder()
        print self.value,
        return 
        
    def preOrder(self):
        if self == None:
            return
        print self.value,
        if self.left != None:
            self.left.preOrder()
        if self.right != None:
            self.right.preOrder()
        return
        
    def inOrder(self):
        if self == None:
            return
        if self.left != None:
            self.left.inOrder()
        print self.value, 
        if self.right != None:        
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
            print "\n"
        return
        
    def preOrder(self):
        if self.root == None:
            return None
        else:
            self.root.preOrder()
            print "\n"
        return
        
    def inOrder(self):
        if self.root == None:
            return None
        else:
            self.root.inOrder()
            print "\n"
        return
        
def main():
    array = []
    for i in range(0, 10):
        array.append(random.randint(0, 100))
    print array
    tree = BST()
    for i in array:
        tree.insert(i)
    tree.inOrder()
    tree.preOrder()
    tree.postOrder()
    
if __name__ == "__main__":
    main()