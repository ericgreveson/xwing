class Ship:
    """
    This represents a ship model (small or large)
    """
    def __init__(self, actions, attack, agility, max_hull, max_shield):
        """
        Constructor
        actions: List of actions that the ship can perform by default
        attack: Default attack strength of primary weapon
        agility: Ship's agility (evade-ness)
        max_hull: Maximum (and initial) hull for this ship
        max_shield: Maximum (and initial) shield for this ship
        """
        # Set up properties
        self.actions = actions
        self.attack = attack
        self.agility = agility
        self.max_hull = max_hull
        self.max_shield = max_shield

        # And our initial health
        self.hull = max_hull
        self.shield = max_shield

        # Set initial position of the ship centre
        self.position = (0, 0)
        self.orientation = 0 # degrees

