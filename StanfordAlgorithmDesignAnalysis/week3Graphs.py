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
            combine(graph, z, x)
            delKey(graph, z)
            i += 1
            removeSelfLoops(graph, x)
        else:
            continue
    return

def removeSelfLoops(graph, node):
    while node in graph[node]:
        indexToRemove = graph[node].index(node)
        graph[node].pop(indexToRemove)

def combine(graph, toReplace, node):
    i = graph[toReplace]
    for j in i:
        if j not in graph[node]:
            graph[node].append(j)
    for i in range(1, 201):
        if i in graph:
            while (True):
                if toReplace in graph[i]:
                    print toReplace
                    print node
                    indexToReplace = graph[i].index(toReplace)
                    print "index", indexToReplace
                    graph[i][indexToReplace] = node
                else:
                    break


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