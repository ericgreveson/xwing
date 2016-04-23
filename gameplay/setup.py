from models.faction import Faction

import json
import os
import random

class Setup:
    """
    This represents the setup phase, before the game proper begins.
    """
    POINT_LIMIT = 100

    def __init__(self, game):
        """
        Constructor
        game: The game to set up
        """
        self._game = game

    def execute(self):
        """
        Run the setup phase of the game
        """
        self._select_squads()
        self._determine_initiative()
        self._place_obstacles()
        self._deploy_forces()

    def _select_squads(self):
        """
        Select squad lists
        """
        for player in self._game.players:
            valid = False
            while not valid:
                # Ask the player for their XWS file and load it
                xws_file = player.choose_squad_list()
                pilots = self._load_squad_xws(xws_file)

                # Check they're all in the right faction, and points is <= point limit
                correct_faction = all([pilot.faction == player.faction for pilot in pilots])
                below_points_limit = sum([pilot.total_points() for pilot in pilots]) <= Setup.POINT_LIMIT
                valid = correct_faction and below_points_limit

            self._game.board.pilots += pilots

    def _determine_initiative(self):
        """
        Figure out who has Initiative
        """
        # Player with the lowest squad point total chooses initiative.
        # If tied, randomly determine this.
        squad_points = [sum([pilot.total_points() for pilot in player.pilots()]) for player in self._game.players]
        if squad_points[0] < squad_points[1]:
            wants_initiative = self._game.players[0].choose_initiative()
            player_with_initiative = 0 if wants_initiative else 1
        elif squad_points[1] < squad_points[0]:
            wants_initiative = self._game.players[1].choose_initiative()
            player_with_initiative = 1 if wants_initiative else 0
        else:
            # Determine initiative randomly
            player_with_initiative = random.randint(0, 1)

        # Set initiative
        for player_index, player in enumerate(self._game.players):
            player.has_initiative = True if player_index == player_with_initiative else False

        print("{0} player has initiative!".format(self._game.players[player_with_initiative].faction.name.capitalize()))

    def _place_obstacles(self):
        """
        Place asteroids and debris fields
        """
        pass

    def _deploy_forces(self):
        """
        Place squads on the board
        """
        for player in self._game.players:
            # Ask the player for their setup file and load it
            setup_file = player.choose_squad_setup()
            self._load_squad_setup(player, setup_file)

    def _load_squad_xws(self, xws_file):
        """
        Load an XWS file defining a squad
        xws_file: The XWS file to load
        return: List of pilots
        """
        pilots = []
        with open(xws_file) as f:
            data = json.load(f)
            for pilot in data["pilots"]:
                pilot_name = pilot["name"]
                upgrades = pilot["upgrades"] if "upgrades" in pilot else []
                pilots.append(self._game.pilot_registry.create(pilot_name, upgrades))

        return pilots

    def _load_squad_setup(self, player, json_file):
        """
        Load the initial board setup for the given player from file
        player: The player to load board setup for
        json_file: The JSON file name to load the setup from
        Format:
        {
          "rebel": [
            {
              "pilot": "rookiepilot",
              "position": [ 874, 874 ],
              "orientation": 0
            }
          ]
        }
        """
        with open(json_file) as f:
            data = json.load(f)
            for faction_name in data:
                if faction_name != player.faction.name:
                    raise ValueError("Faction {0} doesn't match player's faction ({1})".format(faction_name, player.faction.name))

                pilot_list = data[faction_name]
                for pilot_index, pilot in enumerate(player.pilots()):
                    # Check that this ship matches what we expect
                    pilot_data = pilot_list[pilot_index]
                    if pilot_data["pilot"] != pilot.name:
                        raise ValueError("Expecting pilot {0}, found {1}".format(pilot.name, pilot_data["pilot"]))

                    # Set its position and orientation
                    pilot.ship.position = pilot_data["position"]
                    pilot.ship.orientation = pilot_data["orientation"]