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

    def __str__(self):
        """ String representation of the class
		"""

        summary = "Slot: " + self.slot + "Model: " + self.model

        return summary
