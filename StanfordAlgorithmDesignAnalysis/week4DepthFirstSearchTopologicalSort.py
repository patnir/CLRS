# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 18:40:39 2016

@author: Rahul Patni
"""

# Topological Sort Depth First Search

def loadGraph():
    graph = dict()
    filename = "Graph3DFSSTopologicalSort.txt"
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
    
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return 

current_label = 0

def DFSSort(graph):
    global current_label 
    current_label = len(graph.keys()) - 1
    for i in graph.keys():
        if graph[i][1] == False:
            DFS(graph, i)
    return
    
def DFS(graph, start):
    global current_label
    graph[start][1] = True
    for i in graph[start][0]:
        if graph[i][1] == False:
            DFS(graph, i)
    graph[start][2] = current_label
    current_label -= 1
    return

def main():
    graph = loadGraph()
    DFSSort(graph)
    printGraph(graph)
    
if __name__ == "__main__":
    main()