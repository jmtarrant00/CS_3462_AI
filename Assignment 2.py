# Name:         Jonathan Tarrant
# Assignment:   02
# Section:      01
# Due Date:     10/17/2022

#imports
import random
import math as math
import numpy as np

board = [[0,0,0],[0,0,0],[0,0,0]]
print(np.matrix(board))

nums = random.sample(range(1,9), 8)
print(nums)
count = 0
for x in range(3):
    for y in range(3):
        if x == 1 and y == 1:
            continue
        else:
            board[x][y] = nums[count]
            count += 1

print(np.matrix(board))
# for x in range(len(board)):
#     for y in range(len(board[x])):
#         print(f"board[{x}][{y}]: {board[x][y]}")
