import random
import time
import os

clear = lambda: os.system("cls")


def random_state(width: int, height: int) -> list:
    board = []
    chance_of_alive = 0.5
    
    
    for i in range(height):
        board.append([])
        
        for j in range(width):
            random_number = random.random()
            if random_number >= chance_of_alive:
                state = 1
            else:
                state = 0
            
            
            board[i].append(state)
    
    return board



def render(board_state: list):
    top_line = "--"
    for x in range(len(board_state[0])):
        top_line = top_line + "--"

    board_string = top_line + "\n"

    # print(top_line)
    for i in range(len(board_state)):
        board_string += "|"

        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                p = "#"
            else:
                p =" "

            board_string += p + " "
        
        board_string += "|\n"

    board_string += top_line
    return board_string



def next_board_state(board_state: list):
    # Goes through each coordinate of the board
    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            alive_around = 0
            # Goes around the given coordinate
            for y in [-1,0,1]:
                for x in [-1,0,1]:
                    
                    if x == 0 and y == 0:
                        # Won't count it's own coordinate
                        continue
                    elif i+y < 0 or j+x < 0:
                        # Wont wrap around
                        continue

                    try:
                        if board_state[i+y][j+x] == 1:
                            alive_around += 1
                    except:
                        continue
            
            if board_state[i][j] == 1:
                if alive_around <= 1:
                    board_state[i][j] = 0
                elif alive_around <= 3:
                    board_state[i][j] = 1
                else:
                    board_state[i][j] = 0
            else:
                if alive_around == 3:
                    board_state[i][j] = 1
                else:
                    board_state[i][j] = 0


    return board_state


def count_alive(board_state: list):
    alive = 0
    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                alive += 1
    return alive


def eternal_life(board_state: list):
    rounds = 0
    total_cells = count_alive(board_state)
    while True:
        # It kinda skips printing out the first board
        rounds += 1
        board_state = next_board_state(board_state)
        current_alive = count_alive(board_state)
        total_cells += current_alive
        board_render = render(board_state)
        clear()
        print("rounds: ", rounds)
        print("alive: ", current_alive)
        print("average alive: %.2f" % (total_cells/rounds) )
        print(board_render)
        time.sleep(0.1)


# w = int(input("width: "))
# h = int(input("height: "))

# board = random_state(w,h)
# eternal_life(board)
