# 8-puzzle-search

Run with command:
```python test.py```

## To change to 15-puzzle-search ##
In file [test.py](https://github.com/bralpdx/8-puzzle-search/blob/master/test.py) uncomment the ```start_seq``` and ```goal_seq``` variables that correspond with the 15-puzzle.

Then comment out ```start_seq``` and ```goal_seq``` that correspond with 8-puzzle.

```
# Uncomment these variables for the 15 puzzle
# Also change ROWS and COLS values in file environment.py
# start_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# goal_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 8 puzzle
start_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
```


```
# Uncomment these variables for the 15 puzzle
# Also change ROWS and COLS values in file environment.py
start_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
goal_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 8 puzzle
# start_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# goal_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

In the file [environment.py](https://github.com/bralpdx/8-puzzle-search/blob/master/environment.py) change the values of ```COLS``` and ```ROWS``` to ```4```.

```
# Change ROWS and COLS values for N dimensions
COLS = 3
ROWS = 3
```
```
# Change ROWS and COLS values for N dimensions
COLS = 4
ROWS = 4
```

## Description ##
This program implements the A* Search, and Greedy-Best-First Search algorithms on an N-Puzzle (Only tested on 8 and 15 puzzles).

By running the file [test.py](https://github.com/bralpdx/8-puzzle-search/blob/master/test.py)
you will be presented with the starting sequence, solution sequence, number of steps taken, and elapsed time of these algorithms being ran
with 3 different heuristics:

h1 = Manhattan Distance

h2 = Number of displaced tiles

h3 = Combined heuristic, that returns minimum of h1, h2, and a heuristic that takes the average number of misplaced tiles per row.
