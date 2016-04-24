from actions.action_registry import ActionRegistry

from models.bearing_registry import BearingRegistry
from models.dial import Dial
from models.faction import Faction
from models.large_ship import LargeShip
from models.small_ship import SmallShip

import json

class ShipRegistry:
    """
    Registry of ship classes
    """
    SHIP_CLASSES = [SmallShip, LargeShip]

    class ShipPrototype:
        """
        Ship prototype, to be used for constructing ship instances
        """
        pass

    def __init__(self, registry_json_file):
        """
        Constructor
        registry_json_file: The JSON file to load ship descriptions from
        """
        self._ship_prototypes = {}
        with open(registry_json_file) as f:
            data = json.load(f)
            for ship_type in data["ship_types"]:
                # Parse ship details
                name = ship_type["name"]

                ship_dial = ship_type["dial"]
                green = [BearingRegistry.named_bearing_from_string(bearing_name) for bearing_name in ship_dial["green"]]
                white = [BearingRegistry.named_bearing_from_string(bearing_name) for bearing_name in ship_dial["white"]]
                red = [BearingRegistry.named_bearing_from_string(bearing_name) for bearing_name in ship_dial["red"]]

                prototype = ShipRegistry.ShipPrototype()
                prototype.ship_class = ShipRegistry._ship_class_from_string(ship_type["class"])
                prototype.faction = Faction[ship_type["faction"]]
                prototype.actions = [ActionRegistry.action_class_from_string(action_name) for action_name in ship_type["actions"]]
                prototype.dial = Dial(green, white, red)

                # Place in the registry
                self._ship_prototypes[name] = prototype

    def create(self, name):
        """
        Create a ship from its name
        name: The name of the ship type to create
        return: Instance of the ship
        """
        prototype = self._ship_prototypes[name]
        return prototype.ship_class(
            name,
            prototype.faction,
            prototype.actions,
            prototype.dial)

    @staticmethod
    def _ship_class_from_string(ship_class_name):
        """
        Get the actual class from the named ship class in the registry file
        ship_class_name: The name of the subclass of Ship
        return: The subclass of Ship
        """
        for ship_class in ShipRegistry.SHIP_CLASSES:
            if ship_class.__name__ == ship_class_name:
                return ship_class

        raise ValueError("Unknown ship class: {0}".format(ship_class_name))
