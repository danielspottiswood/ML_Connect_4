class connect4:

    def __init__(self):
        self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.turn = 1
        self.score = 0
        self.last_move = (-1,-1)

    def draw(self):
        if(0 in self.board[0]):
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


    def has_won(self):
        if(check_diagonal(self) or check_vertical(self) or check_horizontal(self)):
            return True
        return False
