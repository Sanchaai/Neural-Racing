from Car import Car
from Neural_Network import Neural_Network

class CarAI(Car):

	def __init__(self, track, nn=None):
		super().__init__(track)

		if nn is None:
			self.nn = Neural_Network(6)
			self.nn.addLayer(4)
			self.nn.addLayer(2)
		else:
			self.nn = nn

	def control(self):
		scans = self.getScans()
		results = self.nn.feedForward([*scans, self.v])
		self.acc = -1 + 2 * results[0]
		self.steer = -1 + 2 * results[1]

	def clone(self):
		new = CarAI(self.track, self.nn.clone())
		new.reset()
		return new
