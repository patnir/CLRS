# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:56:21 2016

@author: Rahul Patni
"""

# Djistra's shortest path algorithm
import sys


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
        minimumLength = sys.maxint
        minimumSource = None
        minimumRoute = None
        for i in X:
            for j in graph[i]:
                if j[0] not in X:
                    if j[0] not in B:
                        B[j[0]] = []
                    if j[1] < minimumLength:
                        minimumLength = A[i] + j[1]
                        minimumSource = i
                        minimumRoute = j[0]
        X.append(minimumRoute)
        A[minimumRoute] = minimumLength
        new_list = list(B[minimumSource])
        B[minimumRoute] = new_list
        B[minimumRoute].append(minimumRoute)
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
    