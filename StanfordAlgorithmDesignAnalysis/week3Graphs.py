# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 00:21:57 2016

@author: Rahul Patni
"""

# week 3 Graphs

import random
import math
import sys
import copy

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
            combine(graph, z, x)
            delKey(graph, z)
            i += 1
            removeSelfLoops(graph, x)
    return

def removeSelfLoops(graph, node):
    while node in graph[node]:
        indexToRemove = graph[node].index(node)
        graph[node].pop(indexToRemove)

def combine(graph, toReplace, node):
    i = graph[toReplace]
    for j in i:
        graph[node].append(j)
    for i in range(1, 201):
        if i in graph:
            while toReplace in graph[i]:
                indexToReplace = graph[i].index(toReplace)
                graph[i][indexToReplace] = node


def delKey(graph, key):
    del graph[key]

def main():
    originalGraph = initializeGraph()
    loadGraph(originalGraph)
    totalIterations = int(len(originalGraph) * math.log(len(originalGraph)))
    minimumCut = sys.maxint
    for i in range(totalIterations):
        print "i:", i, "total:", totalIterations
        graph = copy.deepcopy(originalGraph)
        randomizedContraction(graph)
        total = len(graph[graph.keys()[1]])
        if total < minimumCut:
            minimumCut = total
            print minimumCut
    print "finished", minimumCut
    return
    
if __name__ == "__main__":
    main()