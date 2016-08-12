# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 17:54:38 2016

@author: Rahul Patni
"""

# Kosaraju Two Pass with Stack 

def loadGraph():
    graph = dict()
    filename = "Graph4StrongComponent.txt"
    fptr = open(filename)
    for line in fptr:
        i = line.split("\t")
        if int(i[0]) not in graph:
            graph[int(i[0])] = [[], [], False, "Time", "Leader"]
        for x in range(1, len(i)):
            i[x] = i[x].rstrip()
            if i[x] != "\n":
                if int(i[x]) not in graph:
                    graph[int(i[x])] = [[], [], False, "Time", None]
                graph[int(i[0])][0].append(int(i[x]))
                graph[int(i[x])][1].append(int(i[0]))
    return graph
    
def resetSearch(graph):
    for i in graph.keys():
        graph[i][2] = False 
   
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return 

t = 0

s = None

def DFSLoop(graph):
    global t
    t = 0
    global s
    s = None
    for i in range(len(graph), 0, -1):
        if graph[i][2] == False:
            DFS(graph, i, 0)
#    resetSearch(graph)
#    for i in range(len(graph), 0, -1):
#        if graph[i][2] == False:
#            s = graph[i][3]
#            DFS2(graph, i, 1)            

def DFS2(graph, start, direction):
    global s
    graph[start][4] = s
    graph[start][2] = True
    for i in graph[start][direction]:
        if graph[i][2] == False:
            DFS2(graph, i, direction)
    return

def DFS(graph, start, direction):
    global t
    graph[start][2] = True
    for i in graph[start][direction]:
        if graph[i][2] == False:
            DFS(graph, i, direction)
    t += 1
    graph[start][3] = t
    return


def DFSStack(graph):
    z = 0
    for i in range(len(graph), 0, -1):
        if graph[i][2] == False:           
            stack = []
            trace = []
            stack.append(i)
            graph[i][2] = True
            while len(stack) != 0:
                node = stack.pop()
                trace.append(node)
                for k in graph[node][0]:
                    if graph[k][2] == False:
                        graph[k][2] = True
                        print k
                        stack.append(k)
            print trace
            while len(trace) != 0:
                node = trace.pop()
                z += 1
                graph[node][3] = z
    return

def main():
    graph = loadGraph()
    DFSLoop(graph)
    printGraph(graph)
    print "yolo"
    graph = loadGraph()
    DFSStack(graph)
    printGraph(graph)
    return
    
if __name__ == "__main__":
    main()