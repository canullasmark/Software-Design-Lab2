from random import randint
class Die:
    """This class represents a six-sideddie."""
    def __init__(self):
        """Creates a newdie with a value of 1."""
        self.value =1
    def roll(self):
        """Resets thedie's value to a random number
        between 1 and6."""
        self.value =randint(1, 6)
    def getValue(self):
        """Returns thevalue of the die's top face."""
        returnself.value
    def __str__(self):
        """Returns thestring rep of the die."""
        returnstr(self.getValue())