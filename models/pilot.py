from models.weapon import PrimaryWeapon

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

        # And our active status
        self.active = False

        # And our initial health
        self.shield = shield
        self.damage_cards = []

        # And weapons
        self.primary_weapon = PrimaryWeapon()

        # And token counts
        self._stress = 0
        self._focus = 0
        self._evade = 0

    def total_points(self):
        """
        Get the total squad points for this pilot with its upgrades
        """
        return self._points + sum([upgrade.points for upgrade in self.upgrades])

    def adjust_stress(self, delta):
        """
        Add or remove stress tokens to/from this pilot
        delta: Number of stress tokens to add
        """
        prev_stress = self._stress
        self._stress += delta
        self._stress = max(0, self._stress)
        if prev_stress != self._stress:
            print("Pilot {0} now has {1} stress".format(self.name, self._stress))

    def clean_up(self):
        """
        Perform clean-up phase actions for this pilot
        """
        self._focus = 0
        self._evade = 0

    def available_actions(self):
        """
        Get a list of currently available actions for this pilot
        """
        # TODO: pilot abilities, upgrades, ...
        return self.ship.actions

    def can_perform_action(self):
        """
        Return True if this pilot can perform an action, False otherwise
        """
        return self.available_actions() and not self.is_stressed()

    def is_stressed(self):
        """
        Is this pilot stressed?
        """
        return self._stress > 0

    def damage_count(self):
        """
        Count how much damage (including double-damage cards) this pilot has
        """
        return sum([damage_card.value for damage_card in self.damage_cards])

    def is_alive(self):
        """
        Figure out if this ship's damage cards exceed its hull
        """
        return self.damage_count() < self.hull
    
    def weapon_options(self):
        """
        Get the list of weapons that can be used by this pilot
        return: List of Weapon options to attack with (upgrades and/or primary weapon)
        """
        return [self.primary_weapon]
    
    def attack_bonus(self, attack_range):
        """
        Compute any attack bonus from range when attacking
        attack_range: The range (1, 2 or 3) of the attack
        return: Integer bonus, or 0 if no bonus
        """
        return self.primary_weapon.attack_bonus(attack_range)

    def agility_bonus(self, attack_range):
        """
        Compute any agility bonus when being attacked
        attack_range: The range (1, 2 or 3) of the attack
        return: Integer bonus, or 0 if no bonus
        """
        return 1 if attack_range > 2 else 0