"""
Generates the N-Puzzle environment
based on a goal sequence, and starting sequence.
"""
import random

# Change ROWS and COLS values for N dimensions
COLS = 3
ROWS = 3

# Number of tiles
n_tiles = ROWS * COLS
# Number of shuffle moves
n_shuffle = 30


class Environment:
    def __init__(self, start=[], goal=[]):
        self.c_state = start  # The current state of the board
        self.l_bounds = []  # Left Boundary
        self.r_bounds = []  # Right Boundary
        self.goal = goal
        self.set_bounds()
        self.shuffle()  # Shuffles puzzle to generate a solvable puzzle
        self.board = []

    # Constructs the 3x3 board and
    # populates it with the sequence of values.
    def build_board(self):
        if len(self.c_state) != n_tiles:
            print("Error. Invalid sequence.")
            exit()
        for i in range(ROWS):
            self.board.append([])
            for j in range(COLS):
                self.board[i].append(self.c_state[(i * COLS) + j])

    # Shuffles start state to generate a solvable sequence
    def shuffle(self):
        for i in range(0, n_shuffle):
            blank_index = self.c_state.index(0)
            self.swap(blank_index)

    def swap(self, blank):
        direction = random.randint(0, 3)
        # move blank down
        if blank + COLS < n_tiles and direction == 0:
            temp = self.c_state[blank + COLS]
            self.c_state[blank + COLS] = self.c_state[blank]
            self.c_state[blank] = temp

        # move blank up
        elif blank - COLS >= 0 and direction == 1:
            temp = self.c_state[blank - COLS]
            self.c_state[blank - COLS] = self.c_state[blank]
            self.c_state[blank] = temp

        # move blank left
        elif blank not in self.l_bounds and direction == 2:
            temp = self.c_state[blank - 1]
            self.c_state[blank - 1] = self.c_state[blank]
            self.c_state[blank] = temp

        # move blank right
        elif blank not in self.r_bounds and direction == 3:
            temp = self.c_state[blank + 1]
            self.c_state[blank + 1] = self.c_state[blank]
            self.c_state[blank] = temp

    # Sets the left and right puzzle boundaries
    def set_bounds(self):
        self.l_bounds.append(0)
        self.r_bounds.append(COLS - 1)
        for i in range(0, ROWS - 1):
            self.l_bounds.append(self.l_bounds[i] + ROWS)
            self.r_bounds.append(self.r_bounds[i] + ROWS)

    # Prints current layout to console
    def show_board(self):
        for i in range(ROWS):
            print(self.board[i])
