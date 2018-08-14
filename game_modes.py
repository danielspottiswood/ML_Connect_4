from game_setup import connect4
from heuristics import score, threats
from model import minimax
import copy

def face_off(starting_position, depth1, depth2):
    while(starting_position.has_won() == False and starting_position.draw() == False):
        starting_position.play(minimax(starting_position, depth1, 1))
        if(starting_position.has_won()):
            print("they won")
            break
        starting_position.play(minimax(starting_position, depth2, 2))
    print("")
    print("Final Board Position")
    print("")
    if(starting_position.has_won() and starting_position.turn ==1):
        print("The Winner is Player 2!")
    if(starting_position.has_won() and starting_position.turn ==2):
        print("The Winner is Player 1!")
    if(starting_position.has_won()== False):
        print("It's a Draw!")
    print("")
    starting_position.display_board()

def play_bot():
    depth = input("What level of difficulty do you want(1-6): ")
    board = connect4()
    position = input("Would you like to go first(1) or second(2): ")
    while(position!=2 and position != 1):
        print("Please type 1 or 2 you idiot")
        position = input("Would you like to go first(1) or second(2): ")
    comp_pos = 2
    if position == 2:
        board.play(minimax(board, depth, 1))
        comp_pos = 1
    while(board.has_won() == False and board.draw() == False):
        board.display_board()
        print("")
        spot = input("Where would you like to go: ")
        print("")
        while(spot not in range(8)):
            print("That is not a column!")
            spot = input("Where would you like to go: ")
        while(board.legal_move(spot-1)==False):
            print("That is not a legal move!")
            spot = input("Where would you like to go: ")
        board.play(spot-1)
        if(board.has_won() == True or board.draw() == True):
            break
        board.play(minimax(board, depth, comp_pos))

    print("")
    print("Final Board Position")
    print("")
    if(board.has_won() and board.turn ==1):
        if(comp_pos ==2):
            print("The Winner is NOT you!")
        if(comp_pos ==1):
            print("Fine you won")
    if(board.has_won() and board.turn ==2):
        if(comp_pos ==1):
            print("The Winner is NOT you!")
        if(comp_pos ==2):
            print("Fine you won")
    if(board.has_won()== False):
        print("It's a Draw!")
    print("")
    board.display_board()
