from models.bearing_registry import BearingRegistry
from models.faction import Faction
from models.maneuver import Maneuver

import time

class Activation:
    """
    This class represents the Activation phase of a turn
    """
    def __init__(self, game):
        """
        Constructor
        game: The game under way
        """
        self._game = game

    def execute(self):
        """
        Run the Activation phase
        """
        for pilot in self._game.pilots_by_skill():
            pilot.active = True

            # Apply this pilot's maneuver
            pilot.chosen_maneuver.apply(pilot)

            # Choose an action to perform
            if pilot.can_perform_action():
                chosen_action = self._game.player(pilot.faction).choose_action(pilot)

                # TODO: Do something with this

            pilot.active = False