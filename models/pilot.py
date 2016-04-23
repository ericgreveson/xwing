class Pilot:
    """
    This represents a pilot
    """
    def __init__(self, name, faction, ship, skill, attack, agility, hull, shield, upgrades, points):
        """
        Constructor
        name: The name of the pilot
        faction: The faction that the ship belongs to
		ship: The Ship that this pilot flies
        skill: The pilot's skill
        attack: Default attack strength of primary weapon
        agility: Pilot's agility (evade-ness)
        hull: Hull for this pilot
        shield: Maximum (and initial) shield for this pilot
		upgrades: Upgrades that this pilot has equipped
        points: The squad points for this pilot (excluding upgrades)
        """
        # Set up properties
        self.name = name
        self.faction = faction
        self.ship = ship
        self.skill = skill
        self.attack = attack
        self.agility = agility
        self.hull = hull
        self.max_shield = shield
        self.upgrades = upgrades
        self._points = points

        # And our initial health
        self.shield = shield
        self.damage_cards = []

    def total_points(self):
        """
        Get the total squad points for this pilot with its upgrades
        """
        return self._points + sum([upgrade.points for upgrade in self.upgrades])

    def is_alive(self):
        """
        Figure out if this ship's damage cards exceed its hull
        """
        return sum([damage_card.value for damage_card in self.damage_cards]) < self.hull