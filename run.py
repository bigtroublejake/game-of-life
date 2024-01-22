from game_of_life_funcs import random_state, eternal_life


"""
THIS SHOULD BE RUN IN THE TERMINAL

THERE IS A GOOD CHANCE IT WILL NOT WORK 
IF EVERYTHING IS OUTPUTTED IN AN 'OUTPUT' TAB
"""


w = int(input("width: "))
h = int(input("height: "))

board = random_state(w,h)
eternal_life(board)