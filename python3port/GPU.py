class GPU():
	def __init__(self, card, model):
		self.card = card
		self.model = model
		

	def updateInfo(self, temperature, fanSpeed):
		self.fanSpeed = fanSpeed
		self.temperature = temperature