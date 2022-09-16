# Name:         Jonathan Tarrant
# Assignment:   01
# Section:      01
# Due Date:     09/16/2022

#imports
from cgitb import small
import math as math
from random import randint
import numpy as np

# Set target and start locations
targetX, targetY = randint(0,4), randint(0,4)
searchX, searchY = randint(0,4), randint(0,4)

# Make sure not starting on target
while targetX == searchX and targetY == searchY:
    searchX, searchY = randint(0,4), randint(0,4)
    print("loop")

# Set up board
w, h = 5, 5
board = [[0 for y in range(h)] for x in range(w)]
board[targetX][targetY] = 2 # Set target to 2
board[searchX][searchY] = 1 # Set search to 1

# Euclidean Distance Function
def distance(targetX, targetY, searchX, searchY):
    return math.sqrt(pow((targetX-searchX), 2) + pow((targetY - searchY), 2))

# Find next space
def next(nSearchX, nSearchY):
    if nSearchX == targetX and nSearchY == targetY:
        return 0
        
    distances = list()
    for x in range(4):
        if x == 0 and nSearchX != 0:
            distances.append((distance(targetX, targetY, nSearchX-1, nSearchY), nSearchX-1, nSearchY))
        elif x == 1 and nSearchY != 0:
            distances.append((distance(targetX, targetY, nSearchX, nSearchY-1), nSearchX, nSearchY-1))
        elif x == 2 and nSearchX != 4:
            distances.append((distance(targetX, targetY, nSearchX+1, nSearchY), nSearchX+1, nSearchY))
        elif x == 3 and nSearchY != 4:
            distances.append((distance(targetX, targetY, nSearchX, nSearchY+1), nSearchX, nSearchY+1))
    smallest = distances[0]
    for x in distances:
        if distances[x+1][0] < smallest[0]:
            smallest = distances[x+1]
    next(smallest[1], smallest[2])
        


print("Board: ")
print(np.matrix(board))