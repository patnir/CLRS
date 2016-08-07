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
    filename = "Graph2BFSShortestPath.txt"
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
                  
def main():
    graph = loadGraph()
    printGraph(graph)  
    print BFS(graph, 's', 'e')
if __name__ == "__main__":
    main()