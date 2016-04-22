from actions.focus import Focus
from actions.target_lock import TargetLock
from models.faction import Faction
from models.small_ship import SmallShip

class XWing(SmallShip):
    """
    An X-Wing!
    """
    def __init__(self):
        """
        Constructor
        """
        actions = [Focus, TargetLock]
        super().__init__(actions, attack=3, agility=2, max_hull=3, max_shield=2)
        self.faction = Faction.rebel