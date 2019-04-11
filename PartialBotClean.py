def update_state(board):
    tboard = load_last_state()
    nboard = []
    for i in range(5):
        nboard.append([])
        for j in range(5):
            if ((tboard[i][j] == 'o' and board[i][j] == '-') or
                    (tboard[i][j] == 'd' and board[i][j] == '-') or
                    (tboard[i][j] == 'd' and board[i][j] == 'b')):
                elem = '-'
            elif board[i][j] == 'd' and tboard[i][j] == 'o':
                elem = 'd'
            else:
                elem = tboard[i][j]
            nboard[i].append(elem)
    return nboard

def load_last_state():
    board = None
    try:
        f = open('bot.txt', 'r')
        board = [[j for j in f.readline().strip().split()] for i in range(5)]
    except:
        pass
    if (board == None):
        board = [['o', 'o', 'o', 'o', 'o'] for _ in range(5)]
    return board


def save_state(board):
    f = open('bot.txt', 'w')
    for row in board:
        for elem in row:
            elem = '-' if elem == 'b' else elem
            f.write(elem + ' ')
        f.write('\n')
    f.close()


def next_move_aux(board, tar_cell, cur_cell):
    if tar_cell == cur_cell:
        print("CLEAN")
    if (tar_cell[0] > cur_cell[0]):
        cur_cell[0] = cur_cell[0] + 1
        print("DOWN")
    elif (tar_cell[0] < cur_cell[0]):
        cur_cell[0] = cur_cell[0] - 1
        print("UP")
    elif (tar_cell[1] > cur_cell[1]):
        cur_cell[1] = cur_cell[1] + 1
        print("RIGHT")
    elif (tar_cell[1] < cur_cell[1]):
        cur_cell[1] = cur_cell[1] - 1
        print("LEFT")

def dist_bw(r,c,r1,c1):
    return abs(r-r1)+abs(c-c1)

def cost(r,c,r1,c1):
    dis_frm_corner= min(dist_bw(r1,c1,0,0),dist_bw(r1,c1,0,4),dist_bw(r1,c1,4,0),dist_bw(r1,c1,4,4))
    dis_bw = dist_bw(r,c,r1,c1)
    return dis_frm_corner+dis_bw

def next_move(board, cur_cell):
    board = update_state(board)
    dirt_cells = []
    unknown_cells = []
    r, c = cur_cell[0], cur_cell[1]
    dirt_cell = None
    for i in range(5):
        for j in range(5):
            try:
                if board[i][j] == 'd':
                    dirt_cells.append([i, j])
                elif board[i][j] == 'o':
                    unknown_cells.append([i,j])
            except:
                pass
    if len(dirt_cells) != 0:
        dirt_cells = sorted(dirt_cells, key=lambda p: cost(r,c,p[0],p[1]))
        dirt_cell = dirt_cells[0]
    elif len(unknown_cells) != 0 :
        unknown_cells = sorted(unknown_cells, key=lambda p: cost(r,c,p[0],p[1]))
        dirt_cell = unknown_cells[0]
    if dirt_cell != None:
        next_move_aux(board, dirt_cell, cur_cell)
    save_state(board)


if __name__ == "__main__":
    cur_cell = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(board, cur_cell)

