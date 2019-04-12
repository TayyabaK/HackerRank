#!/bin/python3
from collections import defaultdict

# Complete the evenForest function below.
def evenForest():
    nochild,root = 0,1
    for c in tree[root]:        
        nochild += child_nodes(root,c)
    minEdges = sum([1 if (child[x]+1)%2==0 else 0 for x in child])
    return minEdges

def child_nodes(p,c): # p - parent, c - child
    nochild = 0
    for cc in tree[c]:
        if cc != p:
            nochild += child_nodes(c,cc)+1
    child[c] = nochild
    return nochild

n, m = map(int, input().split())
tree = defaultdict(set)
child = defaultdict(int)
for i in range(m):
    u,v = map(int, input().split())
    tree[u].add(v)
    tree[v].add(u)
print(evenForest())
