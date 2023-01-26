# Name:         Jonathan Tarrant
# Assignment:   02
# Section:      01
# Due Date:     10/17/2022

#imports
import tkinter as tk
from tkinter import ttk, CENTER
import random
import math as math
import numpy as np
import copy
import DFS


#Create root window
root = tk.Tk()

#set window title and size
root.title("Assignment 2")
root.geometry("400x200+150+150")
root.configure(bg="#eeeeee")
runningTxt = tk.StringVar(root, "")

#configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

#set the board, and make the goal
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

boardGoal = [[1,2,3],
             [8,0,4],
             [7,6,5]]

nums = random.sample(range(0,9), 9)
boardVar = tk.IntVar(root, np.matrix(board))

#Initialize other variables
count = 0
run = True
userInput = 0
zeroX, zeroY = 0,0
previousStates = list()

# #print out the menu
# def menu():
#     print('''
# --------Menu--------
# 1: DFS Algorithm
# 2: UCS Algorithm
# 3: BFS Algorithm
# 4: A* AlgorithmX
# 5: Exit Program
#         ''')

#DFS Function
def DFS(board, zeroX, zeroY):
    runningTxt.set("Running DFS")
    print(f"ZeroX: {zeroX}\nZeroY: {zeroY}")
    depthLimit = 4
    print(np.matrix(board))

    previousStates.append(board)
    

    # for i in range(4):
    #     print("In for loop")
    #     if i == 0 and zeroX != 0:
    #         (board[zeroX][zeroY], board[zeroX-1][zeroY]) = (board[zeroX-1][zeroY], board[zeroX][zeroY])
    #         zeroX -= 1
    #         boardVar.set(np.matrix(board))
    #     # if i == 1 and zeroY != 0:



def UCS(board):
    print("Running UCS:\n")
def BFS(board):
    print("Running BFS:\n")
def aStar(board):
    print("Running A*:\n")


for x in range(3):
        for y in range(3):
            if nums[count] == 0:
                zeroX = x
                zeroY = y
            board[x][y] = nums[count]
            count += 1

boardVar.set(np.matrix(board))

spaceLabel = ttk.Label(root, text="")
spaceLabel.grid(column=0, row=0)

dfsBtn = ttk.Button(root, text="Run DFS", command=lambda: DFS(board, zeroX, zeroY))
ucsBtn = ttk.Button(root, text="Run UCS", command=lambda: UCS(board))
bfsBtn = ttk.Button(root, text="Run BFS", command=lambda: BFS(board))
aStarBtn = ttk.Button(root, text="Run A*", command=lambda: aStar(board))
dfsBtn.grid(column=0, row=1)
ucsBtn.grid(column=0, row=2)
bfsBtn.grid(column=0, row=3)
aStarBtn.grid(column=0, row=4)

runningLabel = ttk.Label(root, textvariable=runningTxt, justify=CENTER)
boardLabel = ttk.Label(root, textvariable=boardVar, font=(25))
runningLabel.grid(column=1, row=0, rowspan=2)
boardLabel.grid(column=1, row=2, rowspan=3, sticky=tk.N)


spaceLabel2 = ttk.Label(root, text="")
spaceLabel2.grid(column=0, row=5, columnspan=2)
exitButton = ttk.Button(root, text="Exit Program", command=root.destroy)
exitButton.grid(column=0, row=6, columnspan=2,sticky=tk.S)

root.mainloop()
