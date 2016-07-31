# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 00:21:57 2016

@author: Rahul Patni
"""

# week 3 Graphs

def initializeGraph():
    graph = dict()
    for i in range(1, 201):
        graph[i] = []
    return graph

def main():
    graph = initializeGraph()
    print graph
    return
    
if __name__ == "__main__":
    main()