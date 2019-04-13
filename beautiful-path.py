import sys
from collections import defaultdict

# Complete the shortestReach function below.
def dfs(u,cost):
    table[u][cost] = True
    for v,w in graph[u]:
            if not table[v][w|cost]:
                dfs(v,w|cost)

def min_penalty_path():
    dfs(s,0)
    res = -1
    for i in range(1025):
        if table[d][i]:
            res = i
            break
    print(res)

graph = defaultdict(set)
nm = input().split()
n = int(nm[0])
m = int(nm[1])
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].add((v,w))
    graph[v].add((u,w))
s,d = map(int,input().split())
table = [[False for i in range(1025)] for j in range(n+1)]
min_penalty_path()

