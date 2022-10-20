# Name:         Jonathan Tarrant
# Assignment:   02
# Section:      01
# Due Date:     10/17/2022

#imports
import random
import math as math
import numpy as np
from anytree import node, RenderTree

board = [[0,0,0],[0,0,0],[0,0,0]]
nums = random.sample(range(0,9), 9)
count = 0
run = True
userInput = 0

def menu():
    print('''
--------Menu--------
1: DFS Algorithm
2: UCS Algorithm
3: BFS Algorithm
4: A* Algorithm
5: Exit Program
        ''')

def DFS(board):
    print("Running DFS:\n")

    # swap = 0
    # for x in range(3):
    #     for y in range(3):
    #         if 
    #         # if board[x+1][y] == 0:
    #         #     swap = board[x][y]
    #         #     board[x][y] = board [x+1][y]
    #         # elif board[x][y+1] == 0:
    #         #     swap = board[x][y]
    #         #     board[x][y] = board[x][y+1]
    #         # elif board


def UCS(board):
    print("Running UCS:\n")
def BFS(board):
    print("Running BFS:\n")
def aStar(board):
    print("Running A*:\n")

while run:
    count = 0
    for x in range(3):
        for y in range(3):
            # if x == 1 and y == 1:
            #     continue
            # else:
            board[x][y] = nums[count]
            count += 1

    print(f"Starting Board:\n{np.matrix(board)}")  # type: ignore
    menu()

    userInput = int(input("Enter Option: "))
    if userInput == 1:
        DFS(board)
    elif userInput == 2:
        UCS(board)
    elif userInput == 3:
        BFS(board)
    elif userInput == 4:
        aStar(board)
    elif userInput == 5:
        print("Exiting Program...")
        run = False
        break
    else:
        print("Please input a valid menu option")
    
