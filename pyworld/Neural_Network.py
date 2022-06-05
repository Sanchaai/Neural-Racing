from random import weibullvariate
from random import random, randint
from sys import api_version
from turtle import window_height
from math import exp



def sigmoid(x):
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    else:
        z = exp(x)
        return z / (1 + z)

class Neural_Network:
    def __init__(self, inputsize):
        print("createNeuralNetwork")
        self.inputsize = inputsize
        self.weights = []
        self.biases = []
        self.activations = []
        self.lastLayerSize = inputsize
        self.countLayers = 0
    def mutate(self):
        r = random()
        # print(self.weights,self.biases)
        if r > 0.5:          
            idx0 = randint(0,len(self.weights)-1)
            idx1 = randint(0,len(self.weights[idx0])-1)
            idx2 = randint(0,len(self.weights[idx0][idx1])-1)
            x = ((random() * 2)-1)*0.01
            self.weights[idx0][idx1][idx2] += x
        else:
            idx0 = randint(0,len(self.biases)-1)
            idx1 = randint(0,len(self.biases[idx0])-1)
            x = ((random() * 2)-1)*0.01
            self.biases[idx0][idx1] += x

    def feedForward(self, inputs):
        for layer in range(self.countLayers):
            previousactivations = inputs if layer == 0 else self.activations[layer-1]
            neurons = self.weights[layer]
            for neuron in range(len(neurons)):
                arrows = neurons[neuron]
                activation = 0
                for arrow in range(len(arrows)):
                    weight = arrows[arrow]
                    activation += weight*previousactivations[arrow]
                activation += self.biases[layer][neuron]
                self.activations[layer][neuron] = sigmoid(activation)

        
        return self.activations[self.countLayers-1]

    def addLayer(self, size):
        newweights = []
        newactivations = []
        newbiases = []
        for i in range(size):
            newarrows = []
            for j in range(self.lastLayerSize):
                newarrows.append(4*random()-2)
            newweights.append(newarrows)
            newactivations.append(0)
            newbiases.append(4*random()-2)
        self.weights.append(newweights) 
        self.activations.append(newactivations)
        self.biases.append(newbiases)
        self.lastLayerSize = size
        self.countLayers += 1
        print("addLayer")


nn = Neural_Network(6)
nn.addLayer(4)
nn.addLayer(2)
output = nn.feedForward([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
print(nn.weights)
print(output)