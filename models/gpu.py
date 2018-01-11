"""
GPU class module
"""

class GPU(object):

    """
    A graphic processing unit (GPU) class

    Attributes:
        slot (int): GPU's slot.
        model (str): GPU's model/name.
        temperature (int): GPU's core temperature.
        fanspeed (int): GPU's `%` fan speed.

    """

    def __init__(self, slot, model, value = 0, speed = 0):

        """
        Creates a GPU object
        Temperature and Fanspeed set as 0 by default at instantiation.

        Args:
            slot (int): GPU's slot on system.
            model (str): GPU's name/model.
            value (int): GPU's core temperature value.
            speed (int): GPU's fan speed.
        """

        self.slot = slot
        self.model = model
        self.temperature = value
        self.fanspeed = speed


    @property
    def fanspeed(self):
        """GPU fan speed in percentage"""
        return self._fanspeed

    @fanspeed.setter
    def fanspeed(self, speed):
        self._fanspeed = speed

    @property
    def temperature(self):
        """GPU's core temperature in Celcius"""

        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    def __str__(self):
        """String representation of the class"""

        summary = "Slot: %d Model: %s Temprature: %s Fan Speed: %s " \
        % (self.slot, self.model, self.temperature, self.fanspeed)


        return summary
