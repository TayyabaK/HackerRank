# Python 3 solution to Hacker rank problem Prim's (MST) 
#!/bin/python3

import os
from collections import defaultdict
import heapq

def prim(graph,start):
    N = set([i for i in range(1,n+1)]) # set with all vertices numbers
    T = set() # set for adding MST edges
    B = set([start]) # Set for adding nodes who have beed added to MST
    NdiffB = N-B # Set of nodes that have not been added in MST yet
    cost = 0
    while len(B) != n:
        E = [] # storing edges (w,u,v) w=weight,u E B & v E NdiffB
        for u in B:             
            for v,w in graph[u]: # adjacency list of u
                if v in NdiffB:                  
                  heapq.heappush(E,(w,u,v)) # adding elements in list using heap 
        nedge = heapq.heappop(E) # minimum cost edge 
        B.add(nedge[2]) # add the vertex v of the min edge to B
        NdiffB = N-B # calculate difference of N and B
        T.add(nedge) # add edge to MST 
        cost += nedge[0] # add min cost
    return cost

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    graph = defaultdict(list)
    for x in range(m):
        l = [int(x) for x in input().split()]
        graph[l[0]].append([ l[1], l[2] ])
        graph[l[1]].append([ l[0], l[2] ])
    start = int(input())
    result = prim(graph,start)
    fptr.write(str(result) + '\n')

    fptr.close()
