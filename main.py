from game_setup import connect4
from heuristics import score, threats
from model import minimax
from game_modes import face_off, play_bot
import copy
test = connect4()

#face_off(test,1,5)
play_bot()

#print("PLAY: " + str(minimax(test, 5, 2)))
