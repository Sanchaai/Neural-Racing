from random import random, randint
from math import exp

from copy import deepcopy


def sigmoid(x):
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    else:
        z = exp(x)
        return z / (1 + z)

class Neural_Network:
    def __init__(self, inputsize):
        # print("createNeuralNetwork")
        self.inputsize = inputsize
        self.weights = []
        self.biases = []
        self.activations = []
        self.lastLayerSize = inputsize
        self.countLayers = 0

    def mutate(self, learning_rate: float = 0.2, mutation_chance: float = 0.5) -> None:
        "Adjust the weights and biases randomly"
        "Borrowed with permission from Rafael Urben"
        for layerindex in range(len(self.weights)):
            for neuronindex, _ in enumerate(self.biases[layerindex]):
                if random() <= mutation_chance:
                    self.biases[layerindex][neuronindex] += (learning_rate - (random() * 2 * learning_rate))
            for neuronindex, _ in enumerate(self.weights[layerindex]):
                for nextneuronindex, _ in enumerate(self.weights[layerindex][neuronindex]):
                    if random() <= mutation_chance:
                        self.weights[layerindex][neuronindex][nextneuronindex] += (learning_rate - (random() * 2 * learning_rate))

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

    def clone(self):
        nn = Neural_Network(self.inputsize)
        nn.weights = deepcopy(self.weights)
        nn.biases = deepcopy(self.biases)
        nn.activations = deepcopy(self.activations)
        nn.lastLayerSize = self.lastLayerSize
        nn.countLayers = self.countLayers
        return nn

# nn = Neural_Network(6)
# nn.addLayer(4)
# nn.addLayer(2)
# output = nn.feedForward([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
# print(nn.weights)
# print(output)