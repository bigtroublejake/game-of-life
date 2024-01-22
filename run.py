from game_of_life_funcs import random_state, eternal_life

w = int(input("width: "))
h = int(input("height: "))

board = random_state(w,h)
eternal_life(board)