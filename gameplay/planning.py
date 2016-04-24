class Planning:
    """
    This class represents the Planning phase of a turn
    """
    def __init__(self, game):
        """
        Constructor
        game: The game under way
        """
        self._game = game

    def execute(self):
        """
        Run the Planning phase
        """
        for pilot in self._game.pilots_by_skill():
            # Ask the pilot's player what to do
            pilot.active = True
            pilot.chosen_maneuver = self._game.player(pilot.faction).choose_dial(pilot)
            pilot.active = False