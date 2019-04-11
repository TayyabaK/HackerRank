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
#    while len(dirt_cells) != 0 :
    global dirt_cells
    for i in range(len(dirt_cells)):
        dirt_cells[i][1] = abs(dirt_cells[i][0][0] - cur_cell[0]) + abs(dirt_cells[i][0][1] - cur_cell[1])
    dirt_cells = sorted(dirt_cells, key=lambda cell: cell[1])
    tar_cell = dirt_cells[0][0]
#        while cur_cell != tar_cell:
    if tar_cell != cur_cell:
        cur_cell = next_move_aux(board,tar_cell,cur_cell)
    else:
        board[cur_cell[0]][cur_cell[1]] = '-'
        print("CLEAN")
        dirt_cells.pop(0)
dirt_cells = []

if __name__ == "__main__":
    cur_cell = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    for i in range(5):
        yindices = [j for j, elem in enumerate(board[i]) if elem == 'd']
        for yindex in yindices:
            dirt_cells.append([[i, yindex], 0])
    next_move(cur_cell, board)