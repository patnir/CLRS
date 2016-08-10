# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:56:21 2016

@author: Rahul Patni
"""

# Djistra's shortest path algorithm

def loadGraph():
    graph = dict()
    filename = "Graph5Dijkstra.txt"
    fptr = open(filename)
    for line in fptr:
        line = line.rstrip().split(" ")
        if line[0] not in graph:
            graph[line[0]] = []
        if line[1] not in graph:
            graph[line[1]] = []
        graph[line[0]].append([line[1], int(line[2])])
    return graph
    
def printGraph(graph):
    for i in graph.keys():
        print i, graph[i]
    
def dijkstra(graph, start):
    # Initializing components
    X = [start]
    A = dict()
    A[start] = 0
    B = dict()
    B[start] = []
    while len(X) != len(graph):
        routes = []
        length = []
        source = []
        for i in X:
            
            for j in graph[i]:
                if j[0] not in X:
                    if j[0] not in B:
                        B[j[0]] = []
                    source.append(i)
                    routes.append(j[0])
                    lvw = j[1]
                    length.append(A[i] + lvw)
        shortest = length.index(min(length))
        X.append(routes[shortest])
        A[routes[shortest]] = min(length)
        new_list = list(B[source[shortest]])
        B[routes[shortest]] = new_list
        B[routes[shortest]].append(routes[shortest])
    print "X"
    print X
    print "A"
    print A
    print "B"
    print B
    return

def main():
    graph = loadGraph()
    printGraph(graph)
    dijkstra(graph, 's')
    return
    
if __name__ == "__main__":
    main()
    