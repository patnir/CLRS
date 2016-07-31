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

def loadGraph(graph):
    filename = "MinCut.txt"
    fptr = open(filename)
    for line in fptr:
        i = line.split("\t")
        key = int(i[0])
        print "key", key
        for x in range(1, len(i)):
            if i[x] != "\n":
                graph[key].append(int(i[x]))
            

def main():
    graph = initializeGraph()
    print graph
    loadGraph(graph)
    print graph
    return
    
if __name__ == "__main__":
    main()