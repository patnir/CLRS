# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 16:53:03 2016

@author: Rahul Patni
"""

# two pass attmept 2

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
                    graph[int(i[x])] = [[], [], False, None, None]
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
    
    
def main():
    graph = loadGraph()
    printGraph(graph)
    return
    
if __name__ == "__main__":
    main()