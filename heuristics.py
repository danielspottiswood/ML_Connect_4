from game_setup import connect4

def threat_disjoint(game): # checks for 3 in a row disjoint 
    game.last_move = (row, col)
    points = 0 
    count = 0
    player = 1 
    comp = 2
    space = 0
    for row in range(7):
        count = 0
        if (game.board[row].count(player) < 2):
                continue;
        for col in range(6):
            if (game.board[row][col] == player): 
                if (space <= 1):
                    count++
                    if (count == 3):
                        points+=50
                        break
                else:
                    count = 1
                    space = 0
            elif (game.board[row][col] == comp):
                count = 0
            else:
                if (count != 0):
                    space++
    
    return points 



#Count the number of threats for each player
def threat_count(game):
    threats = 0
    last = game.last_move
    for col in range(7):
        for row in range(6):
            if(game.board[row][col]==0):
                game.last_move = (row, col)
                game.board[row][col] = 1
                if(game.has_won()):
                    threats += 100; 
                    #print("Player 1 Row: " + str(row) + " Col: " + str(col))
                else: 
                    if(row % 2 == 1):
                        threats += 1
                    else:
                        threats += .25
                game.board[row][col] = 2
                if(game.has_won()):
                    threats+= 100
                    #print("Player 2 Row: " + str(row) + " Col: " + str(col))
                else:if(row % 2 == 0):
                        threats -= 1
                    else:
                        threats -= .25
                game.board[row][col] = 0
    game.last_move = last
    return threats

def score(game):
    return threat_count(game)

def threats(game):
    threat_matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    last = game.last_move
    for row in range(6):
        for col in range(7):
            if(game.board[row][col]==0):
                threats = 0
                game.last_move = (row, col)
                game.board[row][col] = 1
                if(game.has_won()):
                    #print("Player 1 Row: " + str(row) + " Col: " + str(col))
                    threats = 1
                game.board[row][col] = 2
                if(game.has_won()):
                    #print("Player 2 Row: " + str(row) + " Col: " + str(col))
                    if(threats == 1):
                        threats = 3
                    else:
                        threats = 2
                game.board[row][col] = 0
                threat_matrix[row][col] = threats
    game.last_move = last
    return threat_matrix


def score_improved(game):
    return threat_count(game)
