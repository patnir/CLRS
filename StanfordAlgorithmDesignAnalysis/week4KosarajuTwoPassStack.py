# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 17:54:38 2016

@author: Rahul Patni
"""

# Kosaraju Two Pass with Stack 

def loadGraph():
    graph = dict()
    filename = "SCC.txt"
    fptr = open(filename)
    for line in fptr:
        line = line.rstrip()
        i = line.split(" ")
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
                        stack.append(k)
            while len(trace) != 0:
                node = trace.pop()
                z += 1
                graph[node][3] = z
    return


def DFSSetLeaderStack(graph):
    total = []
    for i in range(len(graph), 0, -1):
        if graph[i][2] == False:
            s = graph[i][3]
            count = 1
            stack = []
            stack.append(i)
            graph[i][2] = True
            while len(stack) != 0:
                node = stack.pop()
                graph[node][4] = s
                for k in graph[node][1]:
                    if graph[k][2] == False:
                        graph[k][2] = True
                        graph[k][4] = s
                        stack.append(k)   
                        count += 1
            total.append(count)
    print total
    y = sorted(range(len(total)), key=lambda x: total[x])[-5:]
    print y
    return

def main():
    graph = loadGraph()
    DFSStack(graph)
    resetSearch(graph)
    DFSSetLeaderStack(graph)
    return
    
if __name__ == "__main__":
    main()