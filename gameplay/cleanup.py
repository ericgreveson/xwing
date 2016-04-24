class Cleanup:
    """
    This represents the Cleanup phase of the game
    """
    def __init__(self, game):
        """
        Constructor
        game: The game under way
        """
        self._game = game

    def execute(self):
        """
        Run the Cleanup phase
        """
        for pilot in self._game.board.pilots:
            pilot.clean_up()
