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
        pilots_in_activation_order = sorted(self._game.board.pilots, key=self._activation_order_sort_key)
        for pilot in pilots_in_activation_order:
            # Ask the pilot's player what to do
            bearing = self._game.player(pilot.faction).choose_dial(pilot)

            # Apply the maneuver
            movement = Maneuver(bearing.value)
            movement.apply(pilot.ship)

    def _activation_order_sort_key(self, pilot):
        """
        Generate a numeric key for sorting pilots in activation order
        pilot: The pilot to generate the key for
        """
        skill_bonus = 0 if self._game.player(pilot.faction).has_initiative else 0.5
        return pilot.skill + skill_bonus