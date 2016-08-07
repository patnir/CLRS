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
        graph[i[0]] = [[], [False], [None]]
        for x in range(1, len(i)):
            i[x] = i[x].rstrip()
            if i[x] != "\n":
                if i[x] not in graph:
                    graph[i[x]] = [[],[False], [None]]
                graph[i[0]][0].append(i[x])
    return graph
                
def printGraph(graph):
    keys = graph.keys()
    for i in keys:
        print i, graph[i]
    return
    
def BFS2(graph, start, target):
    q = Queue()
    q.enqueue(graph[start])
    graph[start][len(graph[start]) - 1] = True
    prevDist = 0
    if target == start:
        return prevDist
    while q.size != 0:
        node = q.dequeue()
        searches= 0
        print node
        for i in range(0, len(node) - 1):
            print "node", node[i]
            if graph[node[i]][len(graph[node[i]]) - 1] == False:
                graph[node[i]][len(graph[node[i]]) - 1] = True
                thisDist = prevDist + 1
                print "graph node" 
                searches += 1
                if node[i] == target:
                    return thisDist
                q.enqueue(graph[node[i]])
        prevDist += 1
    return -1
  
def BFS(graph, start, target):
    return
                  
def main():
    graph = loadGraph()
    printGraph(graph)  
    # print BFS(graph, 's', 'e')
if __name__ == "__main__":
    main()