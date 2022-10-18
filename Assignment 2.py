# Name:         Jonathan Tarrant
# Assignment:   02
# Section:      01
# Due Date:     10/17/2022

#imports
import random
import math as math
import numpy as np
# import anytree 

board = [[0,0,0],[0,0,0],[0,0,0]]
nums = random.sample(range(1,9), 8)
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

def DFS():
    print("Running DFS:\n")


def UCS():
    print("Running UCS:\n")
def BFS():
    print("Running BFS:\n")
def aStar():
    print("Running A*:\n")

while run:
    count = 0
    for x in range(3):
        for y in range(3):
            if x == 1 and y == 1:
                continue
            else:
                board[x][y] = nums[count]
                count += 1

    print(f"Starting Board:\n{np.matrix(board)}")
    menu()

    userInput = int(input("Enter Option:"))
    if userInput == 1:
        DFS()
    elif userInput == 2:
        UCS()
    elif userInput == 3:
        BFS()
    elif userInput == 4:
        aStar()
    elif userInput == 5:
        print("Exiting Program")
        run = False
        break
    else:
        print("Please input a valid menu option")
    
