from environment import COLS, ROWS, n_tiles
from copy import deepcopy

# Set step limit to avoid infinite loops
MAX_MOVES = 1000


# Sets the left and right puzzle boundaries
def set_bounds():
    bounds = []
    l_bounds = []
    r_bounds = []

    l_bounds.append(0)
    r_bounds.append(COLS - 1)
    for i in range(0, ROWS - 1):
        l_bounds.append(l_bounds[i] + ROWS)
        r_bounds.append(r_bounds[i] + ROWS)
    bounds.append(l_bounds)
    bounds.append(r_bounds)

    return bounds


class Puzzle:
    steps = 0  # Number of steps taken
    bounds = set_bounds()
    l_bounds = bounds[0]  # Left Boundary
    r_bounds = bounds[1]  # Right Boundary

    def __init__(self, start=[], goal=[], choice=""):
        self.start = start
        self.goal = goal
        self.parent = []
        self.h_value = 0  # Heuristic value
        self.g_value = 0  # The number of moves associated with the node
        self.f_value = self.g_value + self.h_value  # Cost function
        self.open = []
        self.closed = []
        self.choice = choice  # Dictates the Heuristic used

    # Checks if solution has been found
    def isFound(self, node):
        if node.start[:n_tiles] == self.goal:
            print("Solution found in %d steps" % self.steps)
            print("Move sequence: ",  node.start[n_tiles:])
            self.show_puzzle(node.start)
            return True
        else:
            self.closed.append(node)  # Adds node to closed list
            return False

    # Prints current layout to console
    def show_puzzle(self, node):
        for i in range(ROWS):
            for j in range(COLS):
                print(node[i*COLS+j], end=" ")
            print()

    def move(self, node):
        blank = node.start.index(0)
        # Generate list of successor nodes
        succ = []
        # Move Blank Up
        if blank - COLS >= 0:
            temp = deepcopy(node.start)
            temp[blank] = temp[blank - COLS]
            temp[blank - COLS] = 0
            temp.append("up")
            s = Puzzle(temp, self.goal)
            s.parent = node
            succ.append(s)

        # Move Blank Down
        if blank + COLS < n_tiles:
            temp = deepcopy(node.start)
            temp[blank] = temp[blank + COLS]
            temp[blank + COLS] = 0
            temp.append("down")
            s = Puzzle(temp, self.goal)
            s.parent = node
            succ.append(s)

        # Move Blank Left
        if blank not in self.l_bounds:
            temp = deepcopy(node.start)
            temp[blank] = temp[blank - 1]
            temp[blank - 1] = 0
            temp.append("left")
            s = Puzzle(temp, self.goal)
            s.parent = node
            succ.append(s)

        # Move Blank Right
        if blank not in self.r_bounds:
            temp = deepcopy(node.start)
            temp[blank] = temp[blank + 1]
            temp[blank + 1] = 0
            temp.append("right")
            s = Puzzle(temp, self.goal)
            s.parent = node
            succ.append(s)
        return succ

    # Implements the Best First search algorithm
    def bestfirst(self):
        found = False
        startingNode = Puzzle(self.start, self.goal)
        self.open.append(startingNode)  # Adds starting state to open list

        while not found and len(self.open) > 0 and self.steps < MAX_MOVES:
            f_values = []
            for i in self.open:
                h_val = self.choose_heuristic(i.start[:n_tiles], self.choice)
                g_val = len(i.start[n_tiles:])  # The number of moves associated with the node
                f = g_val + h_val
                f_values.append(f)

            # Pops node associated with the lowest f-value off open list
            cur_node = self.open.pop(f_values.index(min(f_values)))
            found = self.isFound(cur_node)

            # Generate successors
            successors = self.move(cur_node)
            for node in successors:
                self.open.append(node)

            self.steps += 1

        if not found:
            print("No solution found in %d steps." % self.steps)

    # Implements the A* search algorithm
    def astar(self):
        found = False
        startingNode = Puzzle(self.start, self.goal)
        self.open.append(startingNode)  # Adds starting state to open list

        while len(self.open) > 0 and self.steps < MAX_MOVES:
            f_values = []
            for i in self.open:
                h_val = self.choose_heuristic(i.start[:n_tiles], self.choice)
                g_val = len(i.start[n_tiles:])  # The number of moves associated with the node
                f = g_val + h_val
                f_values.append(f)

            # Pops node associated with the lowest f-value off open list
            cur_node = self.open.pop(f_values.index(min(f_values)))

            # Generate successors
            successors = self.move(cur_node)
            for node in successors:
                found = self.isFound(node)
                if found:
                    return
                node.g_value = len(cur_node.start[n_tiles:]) + node.g_value
                node.h_value = self.choose_heuristic(node.start[:n_tiles], self.choice)
                node.f = node.g_value + node.h_value

                for i in self.closed:
                    if i == node.start[:n_tiles]:
                        break
                for j in self.open:
                    if j == node.start[:n_tiles]:
                        break
                else:
                    self.open.append(node)
            self.steps += 1
            self.closed.append(cur_node)

        if not found:
            print("No solution found in %d steps." % self.steps)

    # Selects a heuristic based on argument given
    def choose_heuristic(self, list, choice):
        # Manhattan Distance
        if choice == "h1":
            return self.heur_manhattan(list)
        # Number of misplaced tiles
        elif choice == "h2":
            return self .heur_misplaced(list)
        # Other
        elif choice == "h3":
            return self.heur_comb(list)
        else:
            print("Invalid Heuristic.")
            exit()

    # Manhattan Distance heuristic
    def heur_manhattan(self, list):
        dist = 0
        for i, item in enumerate(list):
            prev_row, prev_col = int(i / 3), i % 3
            goal_row, goal_col = int(item / 3), item % 3
            dist += abs(prev_row-goal_row) + abs(prev_col - goal_col)
        return dist

    # Number of misplaced tiles heuristic
    def heur_misplaced(self, list):
        misplaced = 0
        for i in range(n_tiles):
            if list[i] != self.goal[i]:
                misplaced += 1
        return misplaced

    # Returns average number of misplaced tiles per row
    def heur_avg_misplaced(self, list):
        misplaced = self.heur_misplaced(list)
        return int(misplaced / ROWS)

    # Returns the lowest value of the 3 heuristics
    def heur_comb(self, list):
        manhat = self.heur_manhattan(list)
        disp = self.heur_misplaced(list)
        avg = self.heur_avg_misplaced(list)

        return min(manhat, disp, avg)
