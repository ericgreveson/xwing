from shapely.geometry import box
from shapely.affinity import rotate, translate

class Ship:
    """
    This represents a ship model (small or large)
    """
    def __init__(self, name, faction, actions, dial):
        """
        Constructor
        name: The name of the ship
        faction: The faction that the ship belongs to
        actions: List of actions that the ship can perform by default
        dial: Dial object describing available bearings and difficulties
        """
        # Set up properties
        self.name = name
        self.faction = faction
        self.actions = actions
        self.dial = dial

        # Set initial position of the ship centre
        self.position = (0, 0)
        self.orientation = 0 # degrees

    def get_base_shape(self):
        """
        Get the base shape of this ship, in board coordinates
        return: Polygon representing this ship
        """
        bx = self.base_size[0] / 2
        by = self.base_size[1] / 2
        base_shape = box(-bx, -by, bx, by)
        base_shape = rotate(base_shape, self.orientation)
        return translate(base_shape, self.position[0], self.position[1])
