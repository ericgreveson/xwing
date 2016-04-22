from models.tie_fighter import TieFighter
from models.x_wing import XWing

class ShipRegistry:
    """
    Registry of ship classes
    TODO: convert this to a data-driven model (instead of adding classes for each ship)
    """
    def __init__(self):
        """
        Constructor
        """
        self._ship_classes = [TieFighter, XWing]
        self._ship_class_dict = {ship_class.__name__: ship_class for ship_class in self._ship_classes}

    def ship_class_from_string(self, ship_name):
        """
        Get a ship class from its name
        ship_name: The name of the ship class
        return: The ship class
        """
        return self._ship_class_dict[ship_name]
