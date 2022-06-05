from Track import *
from Car import *
from CarAI import *
from Monaco import setupMonaco
from Traces import clearTraces, saveTraces
from tqdm import tqdm
from copy import deepcopy
import random
import pickle
import os

# Race between two random cars
# Replace dummy network with your network later
filename = "net.pkl"
track = setupMonaco()
generationSize = 125

cars = []
for i in range(generationSize):
	cars.append(CarAI(track))

if os.path.isfile(filename):
	with open(filename, 'rb') as f:
		cars[0] = pickle.load(f)



def step(car):
	if car.gameOver:
		return False
	else:
		car.control()
		car.move()
		car.updateScore()
		if car.checkCollision() or car.score > 2000:
			car.gameOver = True
			return False

def newCars(oldCars):
	bestCars = deepcopy(oldCars[:10])
	for car in bestCars:
		car.reset()
	nCars = [deepcopy(bestCars[0])]
	for _ in range(generationSize-1):
		car = deepcopy(random.choice(bestCars))
		car.nn.mutate()
		nCars.append(car)
	return nCars

clearTraces()

for gen in range(100):
	print(f"Generation {gen}: ")
	for car in tqdm(cars):
		for timesteps in range(2000):
			if not step(car):
				continue 
	cars.sort(key=lambda car:car.score, reverse=True)
	with open(filename,'wb') as f:
		pickle.dump(cars[0], f)
	saveTraces(cars, generation=gen)
	print(cars[0].score)

	cars = newCars(cars)


print(cars)
for car in cars:
	print(car.score)

for car in cars:
	print(car.score, car.x, car.y, car.getLifetime())
