# Name:         Jonathan Tarrant
# Assignment:   01
# Section:      01
# Due Date:     09/16/2022

#imports
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

# Distance between Function
def distance(targetX, targetY, searchX, searchY):
    return math.sqrt(pow((targetX-searchX), 2) + pow((targetY - searchY), 2))



# run = True
# while run:
#     if searchX == 0 or searchX == 4:
#         if searchY == 0 or searchY == 4:
#             print 


print("Board: ")
print(np.matrix(board))