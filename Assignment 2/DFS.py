import Main
import sys
import numpy as np


class Node:
    def __init__(self, state, parent):
        self.state = state 
        self.parent = parent

class Search:
    def __init__(self, start, startLoc, goal):
        self.start = [start, startLoc]
        self.goal = Node(goal, None)

    def find_neighbors(self, state):
        board, (x, y) = state
        results = []

        if x > 0:
            board1 = np.copy(board)
            board1[x][y] = board[x-1][y]
            board[x-1][y] = 0
            results.append([board1, (x-1,y)])

        if y > 0:
            board1 = np.copy(board)
            board1[x][y] = board1[x][y-1]
            board1[x][y-1] = 0
            results.append([board1, (x,y-1)])
        
        if x < 2: 
            board1 = np.copy(board)
            board1[x][y] = board1[x+1][y]
            board1[x+1][y] = 0
            results.append([board1, (x+1,y)])

        if y < 2:
            board1 = np.copy(board)
            board1[x][y] = board1[x][y+1]
            board1[x][y+1] = 0
            results.append([board1, (x,y+1)])

        return results

    def check_visited(self, state):
        for st in self.explored:
            if (st[0] == state[0]).all():
                return False
        return True

