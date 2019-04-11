def next_move_aux(grid, tar_cell, cur_cell):
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
    return cur_cell

def next_move(cur_cell, board):
    dirt_cell = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                dirt_cell = [i,j]
                break
        if dirt_cell != None:
            break
    if dirt_cell != None:
        if dirt_cell != cur_cell:
            cur_cell = next_move_aux(board,dirt_cell,cur_cell)
        else:
            board[cur_cell[0]][cur_cell[1]] = '-'
            print("CLEAN")

if __name__ == "__main__":
    cur_cell = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(cur_cell, board)