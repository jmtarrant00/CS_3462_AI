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
targetX, targetY = 4, 2#randint(0,4), randint(0,4)
searchX, searchY = 1, 0#randint(0,4), randint(0,4)

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

# Euclidean Distance Function
def distance(targetX, targetY, searchX, searchY):
    return math.sqrt(pow((targetX-searchX), 2) + pow((targetY - searchY), 2))

# Find next space
def next(nSearchX, nSearchY):
    if nSearchX == targetX and nSearchY == targetY:
        print("Solved!")
        return 0
    else:   
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
        print("Distances: " + str(distances))
        smallest = distances[0]
        print("Smallest: " + str(smallest))
        print(distances[1][1])
        for x in range(len(distances)):
            print(distances[x][0])
            if distances[x][0] < smallest[0]:
                print("if")
                smallest = distances[x]

        board[smallest[2]][smallest[1]] = 1
        print("Board:")
        print(np.matrix(board))
        sleep(2)
        
        # next(smallest[1], smallest[2])
        
next(searchX, searchY)