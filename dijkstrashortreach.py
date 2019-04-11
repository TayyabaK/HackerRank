#!/bin/python3

import math
import sys
from collections import defaultdict

# Complete the shortestReach function below.
def shortestReach(graph,n,s):
    D = defaultdict(int)
    while graph:   
        u = min(graph, key = lambda k: graph[k][0])
        if graph[u][0] == math.inf:
            break
        pre_dist = graph[u][0]
        for v,w in graph[u][1]:            
            if v in graph:
                old_dist = graph[v][0]
                new_dist = pre_dist + w
                graph[v][0] = min(new_dist,old_dist)
            else:
                old_dist = D[v]
                new_dist = pre_dist + w 
                D[v] = min(new_dist,old_dist)
        D[u] = pre_dist 
        del graph[u]
    l = []
    for i in range(1,n+1):
        if i != s:
            l.append(D[i] if i in D else -1)        
    print(*l,sep=' ')

t = int(input())

for t_itr in range(t):
    graph = {}
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    for _ in range(m):
        u,v,w = map(int,sys.stdin.readline().split())
        node = graph.get(u,[math.inf,[]])
        node[1].append((v,w))
        graph[u] = node
        node = graph.get(v,[math.inf,[]])
        node[1].append((u,w))
        graph[v] = node
    s = int(input())
    graph[s][0] = 0
    shortestReach(graph,n,s)

        
