from actions.barrel_roll import BarrelRoll
from actions.evade import Evade
from actions.focus import Focus
from models.faction import Faction
from models.small_ship import SmallShip

class TieFighter(SmallShip):
    """
    A TIE Fighter (original)
    """
    def __init__(self):
        """
        Constructor
        """
        actions = [Focus, BarrelRoll, Evade]
        super().__init__(actions, attack=2, agility=3, max_hull=3, max_shield=0)
        self.faction = Faction.imperial