from models.ship import Ship

class SmallShip(Ship):
    """
    This represents a small-base ship
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super().__init__(*args, **kwargs)

        # Set up the base size
        self.base_size = (40, 40)
        self.firing_arc = 80