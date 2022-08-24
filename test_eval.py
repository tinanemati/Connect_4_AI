import math
import numpy as np


def eval(self, env):
    window_length = 4
    res = 0
    # check the rows
    for i in range(6):
        curr_row = list(env.board[i])
        # print(list(env.board[i]))
        for c in range(4):
            window = list(curr_row[c:c+3])
            if window.count(self.position) == 3 and window.count(0) == 1:
                res += 100
            elif window.count(self.position) == 2 and window.count(0) == 2:
                res += 10
            elif window.count(self.position) == 1 and window.count(0) == 3:
                res += 1
            if window.count(self.opponent.position) == 3 and window.count(0) == 1:
                res -= 100
            # elif window.count(self.opponent.position) == 2:
            # 	res -= 10
            # elif window.count(self.opponent.position) == 1:
            # 	res -= 1
    # check column
    for i in range(7):
        curr_column = []  # list(env.board[:i])
        for j in range(6):
            curr_column.append(env.board[j][i])

        for c in range(3):
            window = list(curr_column[c:c+3])
            if window.count(self.position) == 3 and window.count(0) == 1:
                res += 100
            elif window.count(self.position) == 2 and window.count(0) == 2:
                res += 10
            elif window.count(self.position) == 1 and window.count(0) == 3:
                res += 1
            if window.count(self.opponent.position) == 3 and window.count(0) == 1:
                res -= 100
            # elif window.count(self.opponent.position) == 2:
            # 	res -= 10
            # elif window.count(self.opponent.position) == 1:
            # 	res -= 1

    # check right diagonals
    for i in range(-2, 4):
        curr_diagnoal = list(env.board.diagonal(i))
        legnth = 0
        if i == 1 or i == 0:
            length = 3
        elif i == -1 or i == 2:
            length = 2
        else:
            length = 1
        for c in range(length):
            window = curr_column[c:c+3]
            if window.count(self.position) == 3 and window.count(0) == 1:
                res += 100
            elif window.count(self.position) == 2 and window.count(0) == 2:
                res += 10
            elif window.count(self.position) == 1 and window.count(0) == 3:
                res += 1
            if window.count(self.opponent.position) == 3 and window.count(0) == 1:
                res -= 100
            # elif window.count(self.opponent.position) == 2:
            # 	res -= 10
            # elif window.count(self.opponent.position) == 1:
            # 	res -= 1
    # check left diagonals
    flipped_board = np.fliplr(env.board)
    for i in range(-2, 4):
        curr_diagnoal = list(flipped_board.diagonal(i))
        legnth = 0
        if i == 1 or i == 0:
            length = 3
        elif i == -1 or i == 2:
            length = 2
        else:
            length = 1
        for c in range(length):
            window = curr_column[c:c+3]
            if window.count(self.position) == 3 and window.count(0) == 1:
                res += 100
            elif window.count(self.position) == 2 and window.count(0) == 2:
                res += 10
            elif window.count(self.position) == 1 and window.count(0) == 3:
                res += 1
            if window.count(self.opponent.position) == 3 and window.count(0) == 1:
                res -= 100
            # elif window.count(self.opponent.position) == 2:
            # 	res -= 10
            # elif window.count(self.opponent.position) == 1:
            # 	res -= 1

    return res


a = np.array([[1, 1, 0, 0, 2, 2, 2],
                 [1, 2, 0, 2, 0, 0, 2],
                 [2, 1, 0, 2, 1, 0, 1],
                 [2, 2, 0, 2, 2, 1, 1],
                 [1, 1, 0, 2, 0, 1, 0],
                 [1, 0, 0, 2, 2, 1, 0]]
                )
# a_flipped = [[2 2 2 0 0 1 1]
#  			   [2 0 0 2 0 2 1]
#  			   [1 0 1 2 0 1 2]
#  			   [1 1 2 2 0 2 2]
#  			   [0 1 0 2 0 1 1]
#  			   [0 1 2 2 0 0 1]]
# row count answer:

# column count answer:
# {2: 2}
# {2: 2, 1: 3}
# {2: 2, 1: 3}
# {2: 2, 1: 3}
# {2: 2, 1: 4}
# {2: 2, 1: 4, 3: 1}
# {2: 3, 1: 4, 3: 1}

# diagonal answer:

player1 = 1
player = 2
count_player1 = eval(a, 1)
# count_player2 = eval(a, 2)
