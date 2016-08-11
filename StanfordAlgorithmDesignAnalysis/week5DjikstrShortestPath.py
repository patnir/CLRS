# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:56:21 2016

@author: Rahul Patni
"""

# Djistra's shortest path algorithm
import sys


def loadGraph():
    graph = dict()
    filename = "dijkstraData.txt"
    #filename = "Graph5Dijkstra.txt"
    fptr = open(filename)
    for line in fptr:
        line = line.rstrip().split("\t")
        if line[0] not in graph:
            graph[line[0]] = []
        for i in range(1, len(line)):
            location = line[i].split(",")
            if location[0] not in graph:
                graph[location[0]] = []
            graph[line[0]].append([location[0], int(location[1])])
    return graph
    
def printGraph(graph):
    for i in graph.keys():
        print i
    
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
                    if A[i] + j[1] < minimumLength:
                        minimumLength = A[i] + j[1]
                        minimumSource = i
                        minimumRoute = j[0]
        X.append(minimumRoute)
        A[minimumRoute] = minimumLength
        new_list = list(B[minimumSource])
        B[minimumRoute] = new_list
        B[minimumRoute].append(minimumRoute)
    return A

def main():
    graph = loadGraph()
    printGraph(graph)
    A = dijkstra(graph, '1')
    print A
    array = ['t','w','7','37','59','82','99','115','133','165','188','197']
    for i in array:
        if i not in A:
            print "weirds", i
        else:
            print A[i], 
    return
    
if __name__ == "__main__":
    main()
    