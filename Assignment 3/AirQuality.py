# Name:         Jonathan Tarrant
# Assignment:   03
# Section:      01
# Due Date:     09/16/2022

#DATA SOURCE: https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset

import pandas as pd
import tkinter as tk
from tkinter import ttk, CENTER
from random import random

data = pd.read_csv("global air pollution dataset.csv", sep=',')
data.drop('AQI Category', inplace=True, axis=1)

dataset = [tuple(x) for x in data.values]
print(f"Dataset[1]: {dataset[1]}")

root = tk.Tk()
root.title("Should I live here?")
root.geometry("400x200")
root.configure(bg='#EEEEEE')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

def perceptron(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        if row[-1] == 5:
            continue
        else:
            activation += weights[i+1] * row[i]
    return max(0, activation)

def run_perceptron(dataset, weights):
    print(f"Dataset Type: {type(dataset)}")
    prediction = perceptron(dataset, weights)
    print(f"Prediction: {prediction}")
    if prediction <= 0.5:
        print("live there")
        outputLabel.configure(text="Live There")
        return 1
    elif prediction > 0.5:
        print("Don't live there")
        outputLabel.configure(text="Don't Live there")
        return 0
    
def train_weights(weights, dataset, learnRate, n_epoch):
    for epoch in range(n_epoch):
        sumError = 0.0
        for row in dataset:
            prediction = perceptron(row, weights)
            error = row[-1] - prediction
            sumError += error**2
            weights[0] = weights[0] + learnRate * error
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1] + learnRate * error * row[i]
    return weights

def run_userInputs(weights):
    cityDataStr = [enterAQI.get(), enterCO.get(),enterO3.get(), enterNO2.get()]
    cityData = [eval(i) for i in cityDataStr]
    print(cityData)
    run_perceptron(cityData, weights)

weights = [random() for i in range(len(dataset[0]))]
weights[0] = 0
learnRate = 0.5
n_epochs = 10

print(f"Before: {weights}")

weights = train_weights(weights, dataset, learnRate, n_epochs)

print(f"After: {weights}")

info = ttk.Label(root, text="Should I live here?\nBased on AQI", justify=CENTER)
info.grid(column=0, row=0, columnspan=2)

enterAQILabel = ttk.Label(root, text="Input the PM2.5 AQI Value for your city: ")
enterAQI = ttk.Entry(root)
enterAQILabel.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
enterAQI.grid(column=1, row=2)

enterCOLabel = ttk.Label(root, text="Input the CO AQI Value for your city: ")
enterCO = ttk.Entry(root)
enterCOLabel.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
enterCO.grid(column=1, row=3)

enterO3Label = ttk.Label(root, text="Enter O3 AQI Value for your city: ")
enterO3 = ttk.Entry(root)
enterO3Label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
enterO3.grid(column=1, row=4)

enterNO2Label = ttk.Label(root, text="Enter the NO2 AQI Value for your city: ")
enterNO2 = ttk.Entry(root)
enterNO2Label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
enterNO2.grid(column=1, row=5)

calcBtn = ttk.Button(root, text="Calculate", command=lambda: run_userInputs(weights))
calcBtn.grid(column=0, row=6, columnspan=2)

outputLabel = ttk.Label(root, text="", justify=CENTER)
outputLabel.grid(column=0, row=7, columnspan=2)

exitButton = ttk.Button(root, text="Exit", command=root.destroy)

root.mainloop()