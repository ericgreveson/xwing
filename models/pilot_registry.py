from models.faction import Faction
from models.pilot import Pilot
from upgrades.astromech import Astromech
from upgrades.torpedo import Torpedo

import json

class PilotRegistry:
    """
    Registry of ship classes
    """
    # TODO
    UPGRADE_SLOTS = [Torpedo, Astromech]

    class PilotPrototype:
        """
        Pilot prototype, to be used for constructing pilot instances
        """
        pass

    def __init__(self, registry_json_file, ship_registry):
        """
        Constructor
        registry_json_file: The JSON file to load pilot descriptions from
        ship_registry: The ship registry to create ships with
        """
        self._pilot_prototypes = {}
        self._ship_registry = ship_registry

        with open(registry_json_file) as f:
            data = json.load(f)
            for pilot in data["pilots"]:
                # Parse ship details
                name = pilot["name"]

                prototype = PilotRegistry.PilotPrototype()
                prototype.faction = Faction[pilot["faction"]]
                prototype.ship = pilot["ship"]
                prototype.skill = pilot["skill"]
                prototype.attack = pilot["attack"]
                prototype.agility = pilot["agility"]
                prototype.hull = pilot["hull"]
                prototype.shield = pilot["shield"]
                prototype.upgrades = [PilotRegistry._upgrade_slot_from_string(upgrade) for upgrade in pilot["upgrades"]]
                prototype.points = pilot["points"]

                # Place in the registry
                self._pilot_prototypes[name] = prototype

    def create(self, name, upgrades):
        """
        Create a pilot from its name
        name: The name of the pilot to create
        upgrades: The list of upgrades to give the pilot
        return: Instance of the pilot
        """
        prototype = self._pilot_prototypes[name]

        # TODO: check that the list of upgrades is valid for this pilot
        return Pilot(
            name,
            prototype.faction,
            self._ship_registry.create(prototype.ship),
            prototype.skill,
            prototype.attack,
            prototype.agility,
            prototype.hull,
            prototype.shield,
            upgrades,
            prototype.points)

    @staticmethod
    def _upgrade_slot_from_string(upgrade_slot_name):
        """
        Get an upgrade slot from its string name
        """
        for upgrade_slot in PilotRegistry.UPGRADE_SLOTS:
            if upgrade_slot.__name__ == upgrade_slot_name:
                return upgrade_slot

        raise ValueError("Unknown upgrade slot name")
