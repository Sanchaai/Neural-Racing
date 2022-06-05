from Track import *
from Car import *
from CarAI import *
from Monaco import setupMonaco
from Traces import clearTraces, saveTraces

# Race between two random cars
# Replace dummy network with your network later

track = setupMonaco()

cars = []
for i in range(60):
	cars.append(CarAI(track))


def step(car):
	if car.gameOver:
		pass
	else:
		car.control()
		car.move()
		car.updateScore()
		if car.checkCollision() or car.score > 2000:
			car.gameOver = True

for timesteps in range(1000):
	for car in cars:
		step(car)

clearTraces()

saveTraces(cars)

for car in cars:
	print(car.score, car.x, car.y, car.getLifetime())
