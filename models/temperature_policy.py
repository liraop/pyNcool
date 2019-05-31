"""
Temperature and policies related module
"""
import intervals as In

class Profile(object):
    """
    Temperature control profile class
    """

    def __init__(self, name):
        """
        Creates a new temperature Profile

        Args:
            name (str): profile name
        """

        self._name = name

    @property
    def name(self):
        """Profile name"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
