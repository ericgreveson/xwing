from gameplay.activation import Activation
from gameplay.cleanup import Cleanup
from gameplay.combat import Combat
from gameplay.planning import Planning

class Turn:
    """
    This represents a single turn of the game
    """
    def __init__(self, game):
        """
        Constructor
        game: The game to process a turn of
        """
        self._game = game

    def execute(self):
        """
        Run the turn
        """
        # First up: planning phase
        print("PLANNING")
        planning_phase = Planning(self._game)
        planning_phase.execute()

        # Next, activation
        print("ACTIVATION")
        activation_phase = Activation(self._game)
        activation_phase.execute()

        # Then, combat
        print("COMBAT")
        combat_phase = Combat(self._game)
        combat_phase.execute()

        # And cleanup
        print("CLEANUP")
        cleanup_phase = Cleanup(self._game)
        cleanup_phase.execute()
