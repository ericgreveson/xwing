from models.faction import Faction
from models.movement_template import MovementTemplate
from models.ship_registry import ShipRegistry

import json

class Board:
    """
    Game board, on which everything else can be placed
    """
    def __init__(self):
        """
        Constructor
        """
        # Board is 3ft by 3ft
        board_size = 914
        self.dimensions = (board_size, board_size)
        self.ships = []

    def load_board_setup(self, json_file):
        """
        Load the initial board setup from file
        json_file: The JSON file name to load the setup from
        Format:
        {
          "players": {
            "rebel": [
              {
                "ship": "XWing",
                "position": [ 874, 874 ],
                "orientation": 0
              },
              ....
            ],
            "imperial": [
              {
                "ship": "TieFighter",
                ...
              },
              ...
            ]
          }
        }
        """
        ship_registry = ShipRegistry()

        factions = set()
        with open(json_file) as f:
            data = json.load(f)
            for faction_name, ships in data["players"].items():
                faction = Faction(faction_name)
                if faction in factions:
                    raise ValueError("Only one of each type of faction allowed!")
                factions.add(faction)

                for ship in ships:
                    # Get the type of ship and make one
                    ship_class = ship_registry.ship_class_from_string(ship["ship"])
                    ship_instance = ship_class()

                    # Check its faction matches
                    if ship_instance.faction != faction:
                        raise ValueError("Ship faction doesn't match player faction!")

                    # Set its position and orientation
                    ship_instance.position = ship["position"]
                    ship_instance.orientation = ship["orientation"]

                    # Add it to the ship list
                    self.ships.append(ship_instance)

        if len(factions) != 2:
            raise ValueError("Need exactly 2 factions for a valid game!")