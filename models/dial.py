from enum import Enum

class Dial:
    """
    Description of bearings and their difficulties
    """
    class Difficulty(Enum):
        green = 'G'
        white = 'W'
        red = 'R'

    def __init__(self, green, white, red):
        """
        Constructor
        green: List of green bearings
        white: List of white bearings
        red: List of red bearings
        """
        self.green = green
        self.white = white
        self.red = red

    def bearings(self):
        """
        Get a list of all available bearings, together with their colors
        return: a list of [(Bearing, Difficulty), (..., ...), ...]
        """
        all_bearings = []
        all_bearings += [(bearing, Dial.Difficulty.green) for bearing in self.green]
        all_bearings += [(bearing, Dial.Difficulty.white) for bearing in self.white]
        all_bearings += [(bearing, Dial.Difficulty.red) for bearing in self.red]
        return all_bearings