# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 00:21:57 2016

@author: Rahul Patni
"""

# week 3 Graphs

import random

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
        for x in range(1, len(i)):
            if i[x] != "\n":
                graph[key].append(int(i[x]))

def randomizedContraction(graph):
    i = 0
    while len(graph) > 2:
        x = random.randint(1, 200)
        if x in graph:
            y = random.randint(0, len(graph[x]) - 1)
            z = graph[x][y]
            print "z", z
            print "x", x
            delKey(graph, x)
            replaceKey(graph, z, x)
            i += 1
        else:
            continue
    return

def replaceKey(graph, toReplace, node):
    for i in range(1, len(graph) + 1):
        if i in graph:
            if toReplace in graph[i]:
                indexToReplace = graph[i].index(toReplace)
                graph[i][indexToReplace] = node

def delKey(graph, key):
    del graph[key]

def main():
    graph = initializeGraph()
    loadGraph(graph)
    randomizedContraction(graph)
    print graph
    if graph.keys()[0] in graph[graph.keys()[1]]:
        print "yes"
    if graph.keys()[1] in graph[graph.keys()[0]]:
        print "yes2"
    return
    
if __name__ == "__main__":
    main()