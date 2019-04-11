import copy
import math

def heuristic(current):
    h1 = 0
    for i  in range (k):
        for j in range (k):
            tile = current[i][j]
            if tile != 0:
                x,y = goal_indices[tile]
                h1 = h1 + abs(x-i)+ abs(y-j)
    return h1 + math.sqrt(noofmisplacedtiles(current))

def noofmisplacedtiles(current):
    noofMistiles = 0
    for i  in range (k):
        for j in range (k):
            if current[i][j] != goal[i][j]:
                noofMistiles+=1
    return noofMistiles

def index_2d(data, search):
    r,c = -1,-1
    for i in range(k):
        for j in range(k):
          if data[i][j] == search:
              r,c = i,j
              return r,c
    return (r,c)

def l2t(state): #list to hashable tuple
    return tuple(tuple(row) for row in state)

def t2l(state): #tuple to list
    return list(list(row) for row in state)

def Astarsearch(start):
    open = {}
    closed = {}
    open[l2t(start)] = [heuristic(start),[],index_2d(start,0),0] #f(n),path,zero pos, state depth
    count = 0
    while len(open) != 0 :
        count += 1
        key_current = (min(open,key = lambda k:open[k][0]))
        cost,path,pos,depth = open[key_current]
        closed[key_current] = open[key_current]
        r,c = pos[0],pos[1]
        del open[key_current]
        if noofmisplacedtiles(key_current) == 0:
            break
        directions = {'UP':(r-1,c),'LEFT':(r,c-1),'RIGHT':(r,c+1),'DOWN':(r+1,c)}
        for dir in directions:
            indices = directions[dir]
            x, y = indices[0], indices[1]
            if x >= 0 and x < k and y >= 0 and y < k:
                dir_state = t2l(key_current)
                dir_state[r][c],dir_state[x][y] = key_current[x][y],key_current[r][c]
                key_dir_state = l2t(dir_state)
                if key_dir_state not in open and key_dir_state not in closed:
                    heur_dir_st = heuristic(dir_state)
                    cost_dir_st = depth + 1 + heur_dir_st
                    open[key_dir_state] = [cost_dir_st, path + [dir],(x,y),depth+1]

    goal_node = closed[key_goal]
    path,depth = goal_node[1],goal_node[3]
    print(len(path))
    for dir in path:
        print(dir)

k = int(input())
goal = []
start = []
goal_indices={}
tnum = 0
for i in range(k):
    start.append([])
    goal.append([])
    for j in range(k):
        start[i].append(int(input()))
        goal[i].append(tnum)
        goal_indices[tnum] = (i,j)
        tnum+=1
key_goal = l2t(goal)
Astarsearch(start)