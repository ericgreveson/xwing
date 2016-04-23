from actions.barrel_roll import BarrelRoll
from actions.boost import Boost
from actions.evade import Evade
from actions.focus import Focus
from actions.target_lock import TargetLock

from models.faction import Faction
from models.small_ship import SmallShip

import json

class ShipRegistry:
    """
    Registry of ship classes
    """
    SHIP_CLASSES = [SmallShip]
    ACTIONS = [BarrelRoll, Boost, Evade, Focus, TargetLock]

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

                prototype = ShipRegistry.ShipPrototype()
                prototype.ship_class = ShipRegistry._ship_class_from_string(ship_type["class"])
                prototype.actions = [ShipRegistry._action_from_string(action_name) for action_name in ship_type["actions"]]
                prototype.faction = Faction[ship_type["faction"]]
                prototype.attack = ship_type["attack"]
                prototype.agility = ship_type["agility"]
                prototype.hull = ship_type["hull"]
                prototype.shield = ship_type["shield"]

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
            prototype.attack,
            prototype.agility,
            prototype.hull,
            prototype.shield)

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

        raise ValueError("Unknown ship class")

    @staticmethod
    def _action_from_string(action_name):
        """
        Get an action class from its string name
        """
        for action in ShipRegistry.ACTIONS:
            if action.__name__ == action_name:
                return action

        raise ValueError("Unknown action")
