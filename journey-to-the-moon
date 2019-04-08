#!/bin/python3

import math
import os
import random
import re
import sys

def disjoint_sets():  
    set_sizes = []
    sumall = 0
    visited = set()
    for i in range(n):      
        if i not in visited: 
            aset = set()
            que = [i]
            while len(que) != 0:
                curr = que.pop(0)
                if curr not in visited:
                    visited.add(curr)
                    aset.add(curr)                
                    childs = cmap.get(curr,[])
                    for child in childs:
                        que.append(child)
            lens = len(aset)
            set_sizes.append(lens)
            sumall += lens
    for i in range(n-sumall):
        set_sizes.append(1)
    sum = 0;
    result = 0;
    for size in set_sizes:
        result += sum*size
        sum += size   
    return result


np = input().split()
n = int(np[0])
p = int(np[1])
cmap = {}
for _ in range(p):
    a1, a2 = map(int, input().rstrip().split())
    cmap[a1] = cmap.get(a1,[])
    cmap[a2] = cmap.get(a2,[])
    cmap[a1].append(a2)
    cmap[a2].append(a1)

result = disjoint_sets()
print(result)
