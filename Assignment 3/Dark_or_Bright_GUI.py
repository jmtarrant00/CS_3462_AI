import tkinter as tk
from tkinter import CENTER, ttk
from random import random

root = tk.Tk()


root.title("Dark or Bright?")
root.geometry("400x200+50+50")
root.configure(bg='#EEEEEE')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

def perceptron(row, weights):
    activation = weights[0]
    for i in range(len(row) - 1):
        activation += weights[i+1] * row[i]
    print(f"Activation: {activation}")
    return 1.0 if activation >= 0.125 else 0.0

def run_perceptron(dataset, weights, trained):
    numCorrect = 0
    expected = ""
    for row in dataset:
        prediction = perceptron(row, weights)
        print(row)
        predText = "bright" if prediction == 1 else "dark"
        expected = "bright" if row[-1] == 1 else "dark"

        print(f"Expected:   {expected}\n" +  
              f"Prediction: {predText}\n")

        if(expected == predText):
            numCorrect += 1

    outputText = "Number correct: " + str(numCorrect)
    if(trained):
        outputTrained.configure(text=outputText)
    elif(not trained):
        outputUntrained.configure(text=outputText)

def train_weights(weights, train, learnRate, n_epoch):
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = perceptron(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + learnRate * error
            for i in range(len(row) - 1):
                weights[i+1] = weights[i+1] + learnRate * error * row[i]
    print(f"Weights: {weights}")
    return weights

trainingData = [[0,0,0,0, 0],
                [0,1,0,0, 0],
                [0,0,0,1, 0],
                [0,1,1,0, 1],
                [1,0,0,1, 1],
                [0,1,0,1, 1],
                [1,0,1,1, 1],
                [1,1,1,0, 1],]

dataset = [[1,0,0,0, 0],
           [0,0,1,0, 0],
           [1,1,0,0, 1],
           [0,0,1,1, 1],
           [1,0,1,0, 1],
           [0,1,1,1, 1],
           [1,1,0,1, 1],
           [1,1,1,1, 1]]

weights = [random() for i in range(len(trainingData[0]))]
weights[0] = 0
# print("\nBefore Training:")
# print(f"Weights: {weights}\n")
# run_perceptron(dataset, weights)

learnRate = 0.1
n_epoch = 8
# weights = train_weights(weights, trainingData, learnRate, n_epoch, dataset)
# print(f"Weights: {weights}")

# print("\nAfter Training:")
# run_perceptron(dataset, weights)

info = ttk.Label(root, text="Perceptron Training")
info.grid(column=0, row=0, padx=5, pady=5,columnspan=3)


untrainedBtn = ttk.Button(root, text="Run perceptron untrained", command=lambda: run_perceptron(dataset, weights, False))
untrainedBtn.grid(column=0, row=2)


outputUntrained = ttk.Label(root, text="", justify=CENTER)
outputUntrained.grid(column=0, row=3)

outputTrained = ttk.Label(root, text="", justify=CENTER)
outputTrained.grid(column=2, row=4)

trainBtn = ttk.Button(root, text="Train Perceptron", command= lambda: train_weights(weights, trainingData, learnRate, n_epoch))
runTrainedBtn = ttk.Button(root, text="Run Trained Perceptron", command = lambda: run_perceptron(dataset, weights, True))
trainBtn.grid(column=2, row=2)
runTrainedBtn.grid(column=2, row=3)




root.mainloop()
