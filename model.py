from game_setup import connect4
from heuristics import score
import copy
from random import randint

def minimax(game, depth, computer):
    #print("Initial Board:")
    #game.display_board()
    if(computer == 1):
        maxi = -10000
        max_row = []
        for row in range(7):
            #print("For Row Numero: " + str(row))
            if(game.legal_move(row)):
                game_next = copy.copy(game)
                game_next.play(row)
                row_score = minimax_helper(game_next, depth, 1)
                if(row_score > maxi):
                    maxi = row_score
                    max_row = [row]
                if(row_score == maxi):
                    max_row.append(row)
        print("Your Positional Score: " + str(maxi))
        if(len(max_row) == 1):
            return max_row[0]
        for i in range(len(max_row)):
            if(max_row[i] ==3):
                return 3
        else:
            return(max_row[randint(0,len(max_row)-1)])
    if(computer == 2):
        mini = 10000
        min_row = []
        for row in range(7):
            #print("For Row Numero: " + str(row))
            if(game.legal_move(row)):
                game_next = copy.copy(game)
                game_next.play(row)
                row_score = minimax_helper(game_next, depth, 1)
                if(row_score < mini):
                    mini = row_score
                    min_row = [row]
                if(row_score == mini):
                    min_row.append(row)
        print("Yours Positional Score: " + str(mini))
        if(len(min_row) == 1):
            return min_row[0]
        for i in range(len(min_row)):
            if(min_row[i] ==3):
                return 3
        else:
            return(min_row[randint(0,len(min_row)-1)])

def minimax_helper(game, depth, cur_depth):
    #print("Cur Depth " +  str(cur_depth))
    #game.display_board()
    if(game.draw()):
        return 0
    if(game.has_won()):
        if(game.turn == 1):
            #print("We Lost!!")
            return -1000
        return 1000
    if(cur_depth == depth):
        #print(score(game))
        return score(game)
    if(game.turn == 1):
        maxi = -10000
        for row in range(7):
            if(game.legal_move(row)):
                game_next = copy.copy(game)
                game_next.play(row)
                maxi = max(maxi, minimax_helper(game_next, depth, cur_depth + 1))
                #print("This is what we got as the maximum that player 1:")
        return maxi
    if(game.turn == 2):
        mini = 10000
        for row in range(7):
            if(game.legal_move(row)):
                game_next = copy.copy(game)
                game_next.play(row)
                mini = min(mini, minimax_helper(game_next, depth, cur_depth + 1))
        #print("This is what we got as the minimum that player 2:")
        #print(mini)
        return mini
