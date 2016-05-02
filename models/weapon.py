class Weapon:
    """
    This represents a weapon on a ship
    """
    def __init__(self, name, ranges, firing_arc, firing_direction=0):
        """
        Constructor
        name: The name of the weapon, for user display
        ranges: The list of ranges that the weapon can attack at, e.g. [1, 2, 3]
        firing_arc: The weapon's firing arc in degrees (e.g. 80)
        firing_direction: The weapon's firing direction, in degrees (e.g. 180 if a rear arc)
        """
        self.name = name
        self.ranges = ranges
        self.firing_arc = firing_arc
        self.firing_direction = firing_direction

    def attack_bonus(self, attack_range):
        """
        Compute any range bonus on an attack
        attack_range: The range (1, 2 or 3) of the attack
        return: Integer bonus, or 0 if no bonus
        """
        return 1 if attack_range < 2 else 0

class PrimaryWeapon(Weapon):
    """
    This represents a ship's primary weapon
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__("primary", ranges=[1, 2, 3], firing_arc=80)

class PrimaryTurret(PrimaryWeapon):
    """
    This represents a primary weapon turret
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.firing_arc = 360
