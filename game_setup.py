import numpy as np; 
class connect4:

    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.turn = 1
        self.score = 0
        self.last_move = (-1,-1)
        
    def draw(self):
        if (0 in self.board[0]):
            return False
        return True

    def check_diagonal(self):
        n_connected = 1
        row = self.last_move[0]
        col = self.last_move[1]
        i = 1
        while(n_connected<4):
            if(row + i > 5 or col + i > 6):
                break
            if(self.board[row+i][col+1] == self.turn):
                n_connected += 1
            else:
                break
            i += 1
        i = 1
        while(n_connected<4):
            if(row - i < 0 or col - i < 0):
                break
            if(self.board[row-i][col-i] == self.turn):
                n_connected += 1
            else:
                break
            i += 1

        if(n_connected == 4):
            return True

    def check_vertical(self):
        n_connected = 1
        row = self.last_move[0]
        col = self.last_move[1]
        i = 1
        while(n_connected<4):
            if(row + i > 5):
                break
            if(self.board[row+i][col] == self.turn):
                n_connected += 1
            else:
                break
            i += 1
        i = 1
        while(n_connected<4):
            if(row - i < 0):
                break
            if(self.board[row-i][col] == self.turn):
                n_connected += 1
            else:
                break
            i += 1

        if(n_connected == 4):
            return True
            
    def check_horizontal(): 
        board = self.board
        row = self.last_move[0]
        if (self.turn == 1): 
            checkFor = "1111"
        else: 
            checkFor = "2222"
        count = 0
        # HORIZONTAL CHECK 
        string_board = ""
        for index in board[row]: 
            string_board += index; 
        if (string_board.contains(checkFor)):
            return True
        else: 
            return False 

    def has_won(self):
        if(check_diagonal(self) or check_vertical(self) or check_horizontal(self)):
            return True
        return False
    def pickPiece(move): 
        self.board[move[0]][move[1]] = self.turn 

    def switchTurns(self): 
        if (self.turn == 1): 
            self.turn = 2
        else: 
            self.turn = 1 

        