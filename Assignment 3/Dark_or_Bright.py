#Couse: CS 3462 Artificial Intelligence
#Student Name: Jonathan Tarrant
#Student ID: 000-831-487
#Assignment Number: 03
#Due Date: Nov. 28th
#
#

from random import random

def perceptron(row, weights):
    activation = weights[0]
    for i in range(len(row) - 1):
        activation += weights[i+1] * row[i]
    return 1.0 if activation >= 0.25 else 0.0

def run_perceptron(dataset, weights):
    expected = ""
    for row in dataset:
        prediction = perceptron(row, weights)
        print(row)
        predText = "bright" if prediction == 1 else "dark"
        expected = "bright" if row[-1] == 1 else "dark"
        print(f"Expected:   {expected}\n" +  
            f"Prediction: {predText}\n")

def train_weights(weights, train, learnRate, n_epoch, dataset):
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = perceptron(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + learnRate * error
            for i in range(len(row) - 1):
                weights[i+1] = weights[i+1] + learnRate * error * row[i]

        # print(f"During Training (epoch {epoch}):")
        # run_perceptron(dataset, weights)
        # print("Epoch: %d\nLearning Rate: %.3f\nError = %.3f" % (epoch, learnRate, sum_error))
    return weights

trainingData = [[0,0,0,0, 0],
                [0,1,0,0, 0],
                [1,1,0,0, 1],
                [0,1,1,0, 1],
                [1,0,0,1, 1],
                [0,1,0,1, 1],
                [1,0,1,1, 1],
                [1,1,1,0, 1],]

dataset = [[1,0,0,0, 0],
           [0,0,1,0, 0],
           [0,0,0,1, 0],
           [0,0,1,1, 1],
           [1,0,1,0, 1],
           [0,1,1,1, 1],
           [1,1,0,1, 1],
           [1,1,1,1, 1]]

weights = [random() for i in range(len(trainingData[0]))]
weights[0] = 0
print(f"Weights: {weights}")
print("\nBefore Training:")
run_perceptron(dataset, weights)

learnRate = 0.1
n_epoch = 8
weights = train_weights(weights, trainingData, learnRate, n_epoch, dataset)
print(f"Weights: {weights}")

print("\nAfter Training:")
run_perceptron(dataset, weights)

# expected = ""
# for row in dataset:
#     prediction = perceptron(row, weights)
#     print(row)
#     predText = "bright" if prediction == 1 else "dark"
#     expected = "bright" if row[-1] == 1 else "dark"
#     print(f"Expected:   {expected}\n" +  
#           f"Prediction: {predText}\n")
