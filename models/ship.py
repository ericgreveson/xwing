class Ship:
    """
    This represents a ship model (small or large)
    """
    def __init__(self, name, faction, actions, attack, agility, hull, shield):
        """
        Constructor
        name: The name of the ship
        faction: The faction that the ship belongs to
        actions: List of actions that the ship can perform by default
        attack: Default attack strength of primary weapon
        agility: Ship's agility (evade-ness)
        hull: Hull for this ship
        shield: Maximum (and initial) shield for this ship
        """
        # Set up properties
        self.name = name
        self.faction = faction
        self.actions = actions
        self.attack = attack
        self.agility = agility
        self.hull = hull
        self.max_shield = shield

        # And our initial health
        self.shield = shield
        self.damage = []

        # Set initial position of the ship centre
        self.position = (0, 0)
        self.orientation = 0 # degrees

