# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 20:20:22 2016

@author: Rahul Patni
"""

# Computing Strong Components

def loadGraph():
    graph = dict()
    filename = "Graph4StrongComponent.txt"
    fptr = open(filename)
    for line in fptr:
        i = line.split("\t")
        graph[i[0]] = [[], False, None]
        for x in range(1, len(i)):
            i[x] = i[x].rstrip()
            if i[x] != "\n":
                if i[x] not in graph:
                    graph[i[x]] = [[], False, None]
                graph[i[0]][0].append(i[x])
    return graph
    
def DFSLoop():
    return
    
def DFS():
    return
    
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return 
    
def main():
    graph = loadGraph()
    printGraph(graph)
    
if __name__ == "__main__":
    main()