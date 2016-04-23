class Player:
    """
    Base class for players
    """
    def __init__(self, faction, board):
        """
        Constructor
        faction: The faction of this player
        board: The game board
        """
        self.faction = faction
        self._board = board

    def choose_squad_list(self):
        """
        Return an XWS file path representing your squad list
        """
        raise NotImplementedError()

    def choose_initiative(self):
        """
        Return True if you want initiative, False if your opponent should have it
        """
        raise NotImplementedError()

    def choose_squad_setup(self):
        """
        Return a .setup.json file path representing your squad setup
        """
        raise NotImplementedError()
    
    def choose_dial(self, pilot):
        """
        Return a Bearing from the given pilot's ship's dial
        """
        raise NotImplementedError()

    def is_alive(self):
        """
        Figure out whether this player has any ships left, returning True if so
        """
        for pilot in self.pilots():
            if pilot.is_alive():
                return True

        return False

    def pilots(self):
        """
        Get list of this player's ships that are currently on the board
        """
        return [pilot for pilot in self._board.pilots if pilot.faction == self.faction]