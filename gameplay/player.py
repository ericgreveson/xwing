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
        Return a Maneuver from the given pilot's ship's dial
        """
        raise NotImplementedError()
    
    def choose_action(self, pilot):
        """
        Return an action from the given pilot's available_actions(), or None if no action requested
        """
        raise NotImplementedError()

    def choose_attack_target(self, pilot, target_options):
        """
        Return a target from the available targets, or None if no attack requested
        pilot: The pilot doing the attacking
        target_options: List of enemy pilots who are in range of at least one weapon
        """
        raise NotImplementedError()

    def choose_attack_weapon(self, pilot, target, weapon_options):
        """
        Return a weapon to attack the given target with out of the available options
        pilot: The pilot doing the attacking
        target: The enemy pilot being attacked
        weapon_options: The list of weapons that can be chosen
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