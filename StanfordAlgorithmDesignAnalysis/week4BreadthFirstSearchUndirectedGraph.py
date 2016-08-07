# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 15:56:25 2016

@author: Rahul Patni
"""

# breadth frist search undirected graph

# finding total number of components# -*- coding: utf-8 -*-

class Queue():
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = []
        
    def empty(self):
        return len(self.data) == 0
    
    def enqueue(self, c):
        self.data.append(c)
        self.tail += 1
        self.size += 1
        
    def dequeue(self):
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        return x

def loadGraph():
    graph = dict()
    filename = "Graph1BFSUndirectedGraph.txt"
    fptr = open(filename)
    for line in fptr:
        i = line.split("\t")
        graph[i[0]] = [[], False, None]
        for x in range(1, len(i)):
            i[x] = i[x].rstrip()
            if i[x] != "\n":
                if i[x] not in graph:
                    graph[i[x]] = [[], False, None]
                graph[i[0]][0].append(i[x])
    return graph
                
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return
    
  
def BFS(graph, start, target):
    if start not in graph:
        return "yolo"
    if start == target:
        return 0
    q = Queue()
    q.enqueue(start)
    graph[start][1] = True
    graph[start][2] = 0
    while q.size != 0:
        node = q.dequeue()
        for i in graph[node][0]:
            if graph[i][1] == False:
                graph[i][1] = True
                graph[i][2] = graph[node][2] + 1
                if i == target:
                    return graph[i][2]
                q.enqueue(i)
    return "yolo"
                  
def findTotalComponents(graph):
    total = 0
    for i in graph.keys():
        if graph[i][1] == False:
            total += 1
            BFS(graph, i, 'yolo')
    return total
                  
def main():
    graph = loadGraph()
    printGraph(graph)  
    components = findTotalComponents(graph)
    print components
if __name__ == "__main__":
    main()