"""
Run this file to see output of A* and Best-First Search
methods implemented in the file 'eightpuzzle.py'

The file runs both algorithms, with three different Heuristics.
It then outputs the starting state, the completed state after the
methods were ran, along with the total number of steps taken,
the solution sequence, and the elapsed time.
"""

from environment import *
from eightpuzzle import *
from time import perf_counter

# Uncomment these variables for the 15 puzzle
# Also change ROWS and COLS values in file environment.py
# start_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# goal_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 8 puzzle
start_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]

env = Environment(start_seq, goal_seq)
env.build_board()

h1 = "h1"  # Corresponds with Manhattan Distance heuristic
h2 = "h2"  # Corresponds with # of misplaced tiles heuristic
h3 = "h3"  # Corresponds with combined heuristic (minimum of 3 heuristics)

start = env.c_state  # Generates a random solvable 8-puzzle sequence.
puzzle = Puzzle(start, goal_seq, h1)

print("1. Starting A* (Manhattan Distance)...")

puzzle.show_puzzle(start)
start_time = perf_counter()
puzzle.astar()
finish_time = perf_counter()
total_time = finish_time - start_time

print("Time Elapsed: %fs" % total_time)
print("-------------------------------")
print("-------------------------------")

print("2. Starting A* (# Displaced tiles)...")
puzzle = Puzzle(start, goal_seq, h2)

puzzle.show_puzzle(start)
start_time = perf_counter()
puzzle.astar()
finish_time = perf_counter()
total_time = finish_time - start_time

print("Time Elapsed: %fs" % total_time)
print("-------------------------------")
print("-------------------------------")

print("3. Starting A* (Combined Heuristic)...")
puzzle = Puzzle(start, goal_seq, h3)

puzzle.show_puzzle(start)
start_time = perf_counter()
puzzle.astar()
finish_time = perf_counter()
total_time = finish_time - start_time

print("Time Elapsed: %fs" % total_time)
print("-------------------------------")
print("-------------------------------")

print("4. Starting Best-First (Manhattan Distance)...")
puzzle = Puzzle(start, goal_seq, h1)

puzzle.show_puzzle(start)
start_time = perf_counter()
puzzle.bestfirst()
finish_time = perf_counter()
total_time = finish_time - start_time

print("Time Elapsed: %fs" % total_time)
print("-------------------------------")
print("-------------------------------")

print("5. Starting Best-First (# Displaced tiles)...")
puzzle = Puzzle(start, goal_seq, h2)

puzzle.show_puzzle(start)
start_time = perf_counter()
puzzle.bestfirst()
finish_time = perf_counter()
total_time = finish_time - start_time

print("Time Elapsed: %fs" % total_time)
print("-------------------------------")
print("-------------------------------")

print("6. Starting Best-First (Combined heuristic)...")
puzzle = Puzzle(start, goal_seq, h3)

puzzle.show_puzzle(start)
start_time = perf_counter()
puzzle.bestfirst()
finish_time = perf_counter()
total_time = finish_time - start_time

print("Time Elapsed: %fs" % total_time)
print("-------------------------------")
print("-------------------------------")


