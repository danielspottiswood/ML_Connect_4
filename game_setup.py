import copy
import numpy as np
class connect4:

    def __init__(self, *args, **kwargs):
        if(len(args)==0):
            self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
            self.turn = 1
            self.last_move = (-1,-1)
        else:
            self.initialize_from_args(args)

def initialize_from_args(self, args):
    self.board = args[0]
    self.turn = args[1]
    self.last_move = args[2]

def __copy__(self):
    #return connect4(copy.copy(self.board), self.turn, copy.copy(self.last_move))
    return connect4(copy.deepcopy(self.board), self.turn, copy.deepcopy(self.last_move))


def draw(self):
    for i in range(7):
        if(self.board[0][i] == 0):
            return False
    return True

def check_se_diagonal(self, streakSize):
    n_connected = 1
    row = self.last_move[0]
    col = self.last_move[1]
    i = 1
    while(n_connected<streakSize):
        if(row + i > 5 or col + i > 6):
            break
        if(self.board[row+i][col+i] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    i = 1
    while(n_connected<streakSize):
        if(row - i < 0 or col - i < 0):
            break
        if(self.board[row-i][col-i] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    if(n_connected == streakSize):
        return True
    return False
def check_nw_diagonal(self, streakSize):
    n_connected = 1
    row = self.last_move[0]
    col = self.last_move[1]
    i = 1
    while(n_connected<streakSize):
        if(row + i > 5 or col - i < 0):
            break
        if(self.board[row+i][col-i] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    i = 1
    while(n_connected<streakSize):
        if(row - i < 0 or col + i > 6):
            break
        if(self.board[row-i][col+i] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    if(n_connected == streakSize):
        return True
    return False

def check_vertical(self, streakSize):
    n_connected = 1
    row = self.last_move[0]
    col = self.last_move[1]
    i = 1
    while(n_connected<streakSize):
        if(row + i > 5):
            break
        if(self.board[row+i][col] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    i = 1
    while(n_connected<streakSize):
        if(row - i < 0):
            break
        if(self.board[row-i][col] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1

    if(n_connected == streakSize):
        return True

def check_horizontal(self, streakSize):
    n_connected = 1
    row = self.last_move[0]
    col = self.last_move[1]
    i = 1
    while(n_connected<streakSize):
        if(col + i > 6):
            break
        if(self.board[row][col+i] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    i = 1
    while(n_connected<streakSize):
        if(col - i < 0):
            break
        if(self.board[row][col-i] == self.board[row][col]):
            n_connected += 1
        else:
            break
        i += 1
    if(n_connected == streakSize):
        return True
    return False

def has_won(self, streakSize):
    if(self.last_move[0]==-1):
        return False
    if(self.check_se_diagonal(streakSize) or self.check_nw_diagonal(streakSize) or self.check_vertical(streakSize) or self.check_horizontal(streakSize)):
        return True
    return False

def legal_move(self, col):
    if(self.board[0][col] ==0):
        return True
    return False

def play(self, col):
    for i in range(6):
        if(self.board[5-i][col]==0):
            self.board[5-i][col] = self.turn
            self.last_move = (5-i, col)
            if(self.turn == 1):
                self.turn = 2
            else:
                self.turn = 1
            break
def display_board(self):
    for row in self.board:
        print(row)

def rem_last(self):
    if(self.last_move[0]!= -1):
        self.board[self.last_move[0]][self.last_move[1]] = 0
