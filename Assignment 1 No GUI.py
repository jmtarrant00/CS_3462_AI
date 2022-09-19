# Name:         Jonathan Tarrant
# Assignment:   01
# Section:      01
# Due Date:     09/16/2022

#imports
import math as math
from random import randint
from time import sleep
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
board = [[0 for x in range(h)] for y in range(w)]
board[targetY][targetX] = 2 # Set target to 2
board[searchY][searchX] = 1 # Set search to 1
print(np.matrix(board))
print("      ↓")

# Euclidean Distance Function
def distance(targetX, targetY, searchX, searchY):
    return math.sqrt(pow((targetX-searchX), 2) + pow((targetY - searchY), 2))

# Find next space
def next(nSearchX, nSearchY):
    # Base case for recursion
    if nSearchX == targetX and nSearchY == targetY:
        print("   Solved!")
        return 0
    else: 
        sleep(1) # Sleep to make it not instant
        distances = list() # Initialize list of distances
        for x in range(4): # Search the 4 adjacent places for best move
            if x == 0 and nSearchX != 0:
                distances.append((distance(targetX, targetY, nSearchX-1, nSearchY), nSearchX-1, nSearchY))
            elif x == 1 and nSearchY != 0:
                distances.append((distance(targetX, targetY, nSearchX, nSearchY-1), nSearchX, nSearchY-1))
            elif x == 2 and nSearchX != 4:
                distances.append((distance(targetX, targetY, nSearchX+1, nSearchY), nSearchX+1, nSearchY))
            elif x == 3 and nSearchY != 4:
                distances.append((distance(targetX, targetY, nSearchX, nSearchY+1), nSearchX, nSearchY+1))
        
        # Find smallest distance
        smallest = distances[0] 
        for x in range(len(distances)):
            if distances[x][0] < smallest[0]:
                smallest = distances[x]
        
        # Move to closest space
        board[smallest[2]][smallest[1]] = 1
        print(np.matrix(board)) # Make a matrix from the board to look better when printing
        print("      ↓")
        next(smallest[1], smallest[2]) # Recursive call
        
next(searchX, searchY)