def save_state(flag1):
    file = open('tron.txt','w')
    file.write(str(flag1))
    file.close()

def load_state():
    try: 
        file = open('tron.txt','r')
        temp = file.readline()
        return bool(temp)
    except:
        save_state(False)
        return False

def landsize(x,y,cells):
    if x >= 0 and y >= 0 and x < size and y < size and grid[x][y] != '-' or (x,y) in cells:
        return 0
    r = 1
    cells.append((x,y))
    r += landsize(x - 1, y, cells)
    r += landsize(x + 1, y, cells)
    r += landsize(x, y - 1, cells)
    r +=landsize(x, y + 1, cells)
    return r

def min_dis_from_corners(x,y,grid):
    corner_dis = [abs(0-x)+abs(0-y),abs(0-x)+abs(14-y),abs(14-x)+abs(0-y),abs(14-x)+abs(14-y)]
    return min(corner_dis)

def maxLandsizeMove(x,y):
    M,pos_moves = 0, []
    for i in moves.keys():
        X, Y = x + moves[i][0], y + moves[i][1]
        if (X >= 0 and X < size and Y >= 0 and Y < size and grid[X][Y] == '-'):
            m = landsize(X,Y,[])
            min_dis_from_corner = min_dis_from_corners(X,Y,grid)
            if M <= m:
                M = m
                pos_moves.append((i,m,min_dis_from_corner))
    if len(pos_moves)!= 0 :
        pos_moves = list(filter(lambda f:f[1]== M,pos_moves))
        pos_moves = sorted(pos_moves,key = lambda f:f[2])
        print(pos_moves[0][0])

def isCellReachable(rpos,gpos,grid):
    stack = [rpos]
    visited = []
    reachable = False
    explored = []
    while len(stack) != 0 and reachable == False:
        pos = stack.pop(-1)
        visited.append(pos)
        x,y = pos[0], pos[1]
        for i in moves.keys():
            X, Y = x + moves[i][0], y + moves[i][1]
            if (X,Y) == gpos:
                stack,reachable =[],True
                break
            if X >= 0 and X < size and Y >= 0 and Y < size and grid[X][Y] in ['-','*']:
                if (X,Y) not in visited:
                    stack.append((X,Y))
    return reachable

def anyfreecellinquadrant(start_x,end_x,start_y,end_y):
    free_cell = None
    for x in range(end_x,start_x,-1):
        for y in range(end_y,start_y,-1):
            if grid[x][y] == '-':
                free_cell = (x,y)
                break
        if free_cell != None:
            break
    return free_cell

def is_center_blocked():
    flag1,flag2 = True,True
    firstquadcell = anyfreecellinquadrant(0,7,0,7)
    fourquadcell = anyfreecellinquadrant(8,14,8,14)
    if firstquadcell != None and fourquadcell != None:
        flag1 = not isCellReachable(firstquadcell,fourquadcell,grid)
    secquadcell = anyfreecellinquadrant(0,7,8,14)
    thirdquadcell = anyfreecellinquadrant(8,14,0,7)
    if secquadcell != None and thirdquadcell != None:
        flag2 = not isCellReachable(secquadcell,thirdquadcell,grid)
    return (flag1|flag2)

def attack(rpos,gpos,grid):
    x,y = rpos[0],rpos[1]
    min_dist = 250
    r = None
    for i in moves.keys():
        X,Y = x + moves[i][0], y + moves[i][1]
        if X >= 0 and X < size and Y >= 0 and Y < size and grid[X][Y] == '-':
            dis = abs(X-gpos[0]) + abs(Y-gpos[1])
            if min_dist > dis:
                min_dist,r = dis,i
    if r != None:
        print(r)

def free_center_cell(rpos,gpos,grid):
    free_cells = []
    for i in range(7,10):
        for j in range(1,14):
            if grid[i][j] == '-':
                free_cells.append(((i,j),abs(rpos[0]-i)+abs(rpos[1]-j)))
    free_cells = sorted(free_cells,key = lambda f:f[1])
    if len(free_cells)!= 0:
        free_cell = free_cells[0]
        return free_cell[0]
    else:
        return None

def block_center(rpos,gpos,grid):
    center_cell = free_center_cell(rpos,gpos,grid)
    if center_cell != None:
        if landsize(center_cell[0],center_cell[1],[]) > 10:
            attack(rpos,center_cell,grid)
        else:
            maxLandsizeMove(rpos[0],rpos[1])
    else:
        maxLandsizeMove(rpos[0],rpos[1])

import random
size= 15
player = input()
just_blocked = load_state()
r_x,r_y,g_x,g_y = map(int,input().split())
grid = []
moves = {'LEFT':(0,-1),'RIGHT':(0,1),'UP':(-1,0),'DOWN':(1,0)}
for _ in range(size):
    grid.append(list(input()))
if player == 'r':
    x, y = r_x, r_y
else:
    x,y = g_x,g_y
    g_x,g_y = r_x,r_y

if is_center_blocked():
    if just_blocked:
        maxLandsizeMove(x,y)
        save_state(False)
    elif isCellReachable((x,y),(g_x,g_y),grid):
        attack((x,y),(g_x,g_y),grid)        
    else:
        maxLandsizeMove(x,y)        
else:
    block_center((x,y),(g_x,g_y),grid)
    if is_center_blocked():
        save_state(True)

