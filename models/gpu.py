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

    def __init__(self, slot, model, temp = 0, speed = 0, pm = 0 ):

        """
        Creates a GPU object
        Temperature and Fanspeed set as 0 by default at instantiation.

        Args:
            slot (int): GPU's slot on system.
            model (str): GPU's name/model.
            temp (int): GPU's core temperature value.
            speed (int): GPU's fan speed.
            pm (int): GPU's persistence mode status
        """

        self._slot = slot
        self._model = model
        self._temperature = temp
        self._fanspeed = speed
        self._pmode = pm

    @property
    def slot(self):
        """GPU slot in system"""
        return self._slot

    @slot.setter
    def slot(self, slot):
        self._slot = slot

    @property
    def model(self):
        """GPU model"""
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

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

    @property
    def pmode(self):
        """GPU persistence mode"""
        return self._pmode

    @pmode.setter
    def pmode(self, is_enabled):
        self._pmode = is_enabled

    def __str__(self):
        """String representation of the class"""

        summary = "Slot: %d Model: %s Temprature: %s Fan Speed: %s PM: %s" \
        % (self.slot, self.model, self.temperature, self.fanspeed, self.pmode)

        return summary
