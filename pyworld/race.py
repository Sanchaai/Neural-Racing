from Track import *
from Car import *
from CarAI import *
from Monaco import setupMonaco
from Traces import clearTraces, saveTraces
from tqdm import tqdm
import random
import pickle
import os


# Race between two random cars
# Replace dummy network with your network later
filename = os.path.join(os.path.dirname(__file__), "net.pkl")
track = setupMonaco()
generationSize = 50
timestep_count = 5000

cars = []

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

def newCars(old_cars):
	best_cars = old_cars[:5]
	new_cars = [best_cars[0].clone()]
	for _ in range(generationSize-1):
		car = random.choice(best_cars).clone()
		car.nn.mutate()
		new_cars.append(car)
	return new_cars

clearTraces()

if os.path.isfile(filename):
	with open(filename, 'rb') as f:
		loadedcar = pickle.load(f)
	loadedcar.reset()
	cars.append(loadedcar)
	cars = newCars(cars)
else:
	for i in range(generationSize):
		cars.append(CarAI(track))

for gen in range(10):
	print(f"Generation {gen}: ")
	for car in tqdm(cars, desc=f"Gen {gen}"):
		for timestep in range(timestep_count):
			if step(car) == False:
				break 

	cars.sort(key=lambda car:car.score, reverse=True)
	print([c.score for c in cars])
	print(cars[0].score)

	best_car = cars[0]
	best_car.reset()
	with open(filename,'wb') as f:
		pickle.dump(best_car, f)
	saveTraces(cars, generation=gen)

	cars = newCars(cars)


print(cars)
for car in cars:
	print(car.score)

for car in cars:
	print(car.score, car.x, car.y, car.getLifetime())
