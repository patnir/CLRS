# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 12:46:13 2016

@author: Rahul Patni
"""

# Bread-first search shortest path

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
    filename = "Graph1BFSShortestPath.txt"
    fptr = open(filename)
    for line in fptr:
        i = line.split("\t")
        graph[i[0]] = []
        for x in range(1, len(i)):
            i[x] = i[x].rstrip()
            if i[x] != "\n":
                if i[x] not in graph:
                    graph[i[x]] = []
                graph[i[0]].append(i[x])
        graph[i[0]].append(False)
    return graph
                
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        if len(graph[i]) == 0:
            graph[i].append(False)
        print i, graph[i]
    return
    
def BFS(graph, start, target):
    q = Queue()
    q.enqueue(graph[start])
    graph[start][len(graph[start]) - 1] = True
    while q.size != 0:
        node = q.dequeue()
        print node
        for i in range(0, len(node) - 1):
            if graph[node[i]][len(graph[node[i]]) - 1] == False:
                graph[node[i]][len(graph[node[i]]) - 1] = True
                q.enqueue(graph[node[i]])
    printGraph(graph)
    return
          
def main():
    graph = loadGraph()
    printGraph(graph)  
    BFS(graph, 's', 'e')
if __name__ == "__main__":
    main()