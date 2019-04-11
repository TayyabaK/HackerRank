#!/bin/python3

import sys
import heapq

def find_set(x):
    ret = None 
    if (parent[x] == x):
        ret = x
    else:
        parent[x] = find_set(parent[x])
        ret = parent[x]
    return  ret

def is_same_set(u,v):
    return ( find_set(u) == find_set(v))

def union(u,v):
    parent[find_set(u)] = find_set(v)

# Complete the 'kruskals' function below.
def kruskals(n,edges):    
    for i in range(1,n+1):
        parent.append(i)
    sumw,noedges = 0,0
    while noedges != n-1:
        w,u,v = heapq.heappop(edges)
        if not is_same_set(u,v):
            sumw += w
            noedges += 1
            union(u,v)
    return sumw                     
        
n, m = map(int, sys.stdin.readline().split())
edges = [] 
for i in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    heapq.heappush(edges,(w,u,v))
parent = [0]
res = kruskals(n,edges)
print(res)
