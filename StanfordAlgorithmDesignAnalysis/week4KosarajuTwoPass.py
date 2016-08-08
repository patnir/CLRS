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
        graph[int(i[0])] = [[], False, None, None]
        for x in range(1, len(i)):
            i[x] = i[x].rstrip()
            if i[x] != "\n":
                if int(i[x]) not in graph:
                    graph[int(i[x])] = [[], False, None]
                graph[int(i[0])][0].append(int(i[x]))
    return graph
    
# Number of nodes finished exploring
t

# most recent vertes from which DFS was called
# leader for second pass
s

def resetSearch(graph):
    for i in graph.keys():
        graph[i][1] = False

def DFSLoop(graph):
    global s, t
    t = 0
    s = None
    for i in range(len(graph), 0, -1):
        if graph[i][1] == False:
            DFS(graph, i)
    resetSearch(graph)
    for i in range(len(graph), 0, -1):
        if graph[i][1] == False:
            s = i
            DFS2(graph, i)
    return

def DFS2(graph, start):    
    global s
    graph[start][1] = True
    graph[start][3] = s
    for i in graph[start][0]:
        graph[i][3] = start
        if graph[i][1] == False:
            DFS2(graph, i)
    return

def DFS(graph, start):
    global s, t
    graph[start][1] = True
    for i in graph[start][0]:
        if graph[i][1] == False:
            DFS(graph, i)
    t += 1
    graph[start][2] = t
    return
    
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return 
   
def countStrongComponents():
    return

def leaderGraph(graph):
    g = dict()
    for i in graph.keys():
        tail = graph[i][2]
        head = i
        g[tail] = head
    return g
    
def main():
    graph = loadGraph()
    printGraph(graph)
    DFSLoop(graph)
    printGraph(graph)
    lGraph = leaderGraph(graph)
    printGraph(lGraph)
    
    
if __name__ == "__main__":
    main()