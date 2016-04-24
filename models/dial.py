from models.difficulty import Difficulty
from models.maneuver import Maneuver

class Dial:
    """
    Description of bearings and their difficulties
    """
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

    def maneuvers(self):
        """
        Get a list of all available maneuvers
        return: a list of maneuvers
        """
        all_maneuvers = []
        all_maneuvers += [Maneuver(bearing, Difficulty.green) for bearing in self.green]
        all_maneuvers += [Maneuver(bearing, Difficulty.white) for bearing in self.white]
        all_maneuvers += [Maneuver(bearing, Difficulty.red) for bearing in self.red]
        return all_maneuvers

    def maneuver_from_named_bearing(self, named_bearing):
        """
        Get the maneuver for this dial from the given named bearing
        named_bearing: The named bearing to look up
        return: The maneuver for the named bearing
        """
        for maneuver in self.maneuvers():
            if maneuver.named_bearing() == named_bearing:
                return maneuver

        raise ValueError("Bearing {0} not found on dial!".format(named_bearing.name))