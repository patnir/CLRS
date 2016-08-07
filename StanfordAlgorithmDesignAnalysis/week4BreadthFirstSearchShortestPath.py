# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 12:46:13 2016

@author: Rahul Patni
"""

# Bread-first search shortest path

def loadGraph():
    graph = dict()
    filename = "Graph1BFSShortestPath.txt"
    fptr = open(filename)
    for line in fptr:
        i = line.split("\t")
        graph[i[0]] = []
        for x in range(1, len(i)):
            if i[x] != "\n":
                i[x] = i[x].rstrip()
                graph[i[0]].append(i[x])
    return graph
                
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return
    
def BFS(graph, start, target):
    return
          
def main():
    graph = loadGraph()
    printGraph(graph)  
    BFS(graph, 's', 'e')
if __name__ == "__main__":
    main()