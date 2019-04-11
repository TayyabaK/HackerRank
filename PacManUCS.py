# This is the A* algorithm a variation of UCS

explored = {}
open = {}
closed = {}
path = []
rp, cp = map(int, input().split())
rf, cf = map(int, input().split())
h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())
rc,cc = rp,cp
open[(rc,cc)] = [0+abs(rc-rf)+abs(cc-cf),[(rc,cc)]]
while (rc,cc) != (rf,cf):
    min_key_pos = min(open, key=lambda k: open[k][0])
    rc, cc = min_key_pos[0], min_key_pos[1]
    closed[(rc, cc)] = open[rc, cc]
    cost, path = open[(rc, cc)]
    open.pop((rc, cc), None)
    if (rc,cc) == (rf,cf):
        break

    directions = [(rc-1,cc),(rc,cc-1),(rc,cc+1),(rc+1,cc)]
    def is_valid_move(dr):
        return dr[0] >= 0 and dr[0] < h and dr[1] >= 0 and dr[1] < w and grid[dr[0]][dr[1]]!= '%'
    directions = filter(lambda dr: is_valid_move(dr),directions)
    for dr in directions:
        x,y = dr[0],dr[1]
        costdr = len(path) + 1 + abs(x - rf) + abs(y - cf)
        if (x,y) not in open and (x,y) not in closed:
            open[(x,y)] = [costdr,path+[(x,y)]]
        elif (x,y) in closed:
            if costdr < closed[(x,y)][0]:
                oldpath = open[(x,y)][1]
                oldpath.pop(-1)
                newpath = oldpath.append((rc,cc))
                open[(x,y)] = [costdr,newpath]
                closed.pop((x,y),None)

path = closed[(rf,cf)][1]
print(len(path)-1)
for cell in path:
    print(cell[0],cell[1],sep = ' ')

