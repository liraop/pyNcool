class GPU():

	"""
	A graphic processing unit

	"""

	def __init__(self, slot, model):
		"""
		Defines the GPU slot and card model.

		GPU slot is the logical slot of the GPU in the system. If it's a single
		unit, slot is 0. GPU slot is stored in `self.slot`.

		Card model is stored in `self.model`

		"""
		self.slot = slot
		self.model = model


	def updateInfo(self, temperature, fanSpeed):
		""" Updates GPU's information

		Current GPU fan speed is stored at `self.fanSpeed`

		Current GPU temperature is stored at `self.temperature`

		"""
		self.fanSpeed = fanSpeed
		self.temperature = temperature
