import numpy as np
import random


def drawValidBoard():
    b = np.zeros((3, 3, 3, 3), dtype='int')
    for box in range(3):
        temp = random.sample(range(1, 10), 9)
        idx = 0
        for i in range(3):
            for j in range(3):
                b[0 + box][i][0 + box][j] = temp[idx]
                idx += 1
    b = b.reshape((9, 9))
    solve(b)
    return b


def scramble(bo):
    for box_y in [0, 3, 6]:
        for box_x in [0, 3, 6]:
            z = random.choice([4, 5, 6])
            zeros = random.sample(range(9), z)
            zeros = [(i // 3, i % 3) for i in zeros]
            for i, j in zeros:
                bo[box_y + i][box_x + j] = 0


def drawBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- ' * 3 + ' ' + '- ' * 3 + ' ' + '- ' * 3)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('|', end='')
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, column

    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    empty = findEmpty(bo)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, len(bo) + 1 if len(bo) > len(bo[0]) else len(bo[0]) + 1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def randBoard():
    board = drawValidBoard()
    scramble(board)
    return board


def solver(b):
    solve(b)
    return b


# board = drawValidBoard()
# scramble(board)
# drawBoard(board)
# print('************')
# solve(board)
# drawBoard(board)
drawBoard(randBoard())
