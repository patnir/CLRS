# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:38:07 2016

@author: Rahul Patni
"""

class Node():
    def __init__(self, c):
        self.c = c
        self.children = []
        
    def addChild(self, c):
        self.children.append(Node(c))
        
    def printChildren(self):
        print self.c, 

        if len(self.children) == 0:
            return
        for i in self.children:
            i.printChildren()
            
        

class Tree():
    def __init__(self):
        self.firstChildren = []
    
    def searchLevel(self, l, c):
        for i in range(0, len(l)):
            if l[i].c == c:
                return i
        return -1
    
    def printTree(self):
        for i in self.firstChildren:
            i.printChildren()
    
    def add(self, word):
        letters = list(word)
        print letters
        curr = self.firstChildren
        for i in range(0, len(letters)):
            print letters[i]
            position = self.searchLevel(curr, letters[i])
            print position
            if position == -1:
                while i < len(letters):
                    node = Node(letters[i])
                    print node.c
                    curr.append(node)
                    curr = node.children
                    i += 1
                return
            else:
                node = Node(letters[i])
                curr.append(node)
                curr = node.children
                

def main():
    t = Tree()
    t.add("asdd")
    t.printTree()
    
    
main()
        
            
        