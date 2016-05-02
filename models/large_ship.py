from models.ship import Ship

class LargeShip(Ship):
    """
    This represents a large-base ship
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super().__init__(*args, **kwargs)

        # Set up the base size
        self.base_size = (80, 80)