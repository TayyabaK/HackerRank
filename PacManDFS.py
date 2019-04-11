explored = {}
stack = []
tstack = []
path = []
rp, cp = map(int, input().split())
rf, cf = map(int, input().split())
h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())
rc,cc = rp,cp
explored[(rc,cc)] = [0,[(rc,cc)]]
stack.append((rc,cc))
while (rc,cc) != (rf,cf):
    p = stack.pop(-1)
    tstack.append(p)
    rc, cc = p[0], p[1]
    directions = [(rc-1,cc),(rc,cc-1),(rc,cc+1),(rc+1,cc)]
    def is_valid_move(dr):
        return dr[0] >= 0 and dr[0] < h and dr[1] >= 0 and dr[1] < w and (dr[0], dr[1]) not in explored and grid[dr[0]][dr[1]]!= '%'
    directions = filter(lambda dr: is_valid_move(dr),directions)
    depth,path = explored[(rc,cc)]
    for dr in directions:
        x,y = dr[0],dr[1]
        stack.append((x,y))
        explored[(dr[0],dr[1])] = [explored[(rc,cc)][0]+1,path+[(x,y)]]

print(len(tstack))
for cell in tstack:
    print(cell[0],cell[1],sep=' ')
target = explored[(rf,cf)]
print(target[0])
for cell in target[1]:
    print(cell[0],cell[1], sep = ' ')
