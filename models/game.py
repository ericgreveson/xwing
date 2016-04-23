class Game:
    """
    Model for a complete X-Wing game
    """
    def __init__(self, board, players, pilot_registry):
        """
        Constructor
        board: The game board representing the game state
        players: The list (of length two) of players
        pilot_registry: The pilot registry
        """
        self.board = board
        self.players = players
        self.pilot_registry = pilot_registry

    def player(self, faction):
        """
        Get the player for the given faction
        faction: The faction to get the player for
        return: The player of the given faction
        """
        for player in self.players:
            if player.faction == faction:
                return player

        raise ValueError("Given faction is not playing!")

    def is_over(self):
        """
        Is the game over?
        """
        return not all([player.is_alive() for player in self.players])