class Ship:
    """
    This represents a ship model (small or large)
    """
    def __init__(self, name, faction, actions, dial):
        """
        Constructor
        name: The name of the ship
        faction: The faction that the ship belongs to
        actions: List of actions that the ship can perform by default
        dial: Dial object describing available bearings and difficulties
        """
        # Set up properties
        self.name = name
        self.faction = faction
        self.actions = actions
        self.dial = dial

        # Set initial position of the ship centre
        self.position = (0, 0)
        self.orientation = 0 # degrees