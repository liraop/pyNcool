"""
GPU class module
"""

class GPU(object):

    """
    A graphic processing unit (GPU) class
    """

    def __init__(self, slot, model):

        """
        Creates a GPU object

        Attributes:
            slot (int): GPU's slot.
            model (str): GPU's name/model.
        """

        self.slot = slot
        self.model = model

        self.fanspeed = None
        """ int: GPU's fanspeed """

        self.temperature = None
        """ int: GPU's temperature in Celcius """

    def update_info(self, temperature, fanspeed):
        """ Updates GPU's information

		Current GPU fan speed is stored at `self.fanSpeed`

		Current GPU temperature is stored at `self.temperature`

		"""
        self.fanspeed = fanspeed
        self.temperature = temperature

    def __str__(self):
        """ String representation of the class
		"""

        summary = "Slot: " + self.slot + "Model: " + self.model

        return summary
