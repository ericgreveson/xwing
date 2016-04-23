from models.bearing import Bearing
from models.movement_template import MovementTemplate

from enum import Enum

class BearingRegistry(Enum):
    """
    List of all bearings that can be used for maneuvers etc
    """
    # Straight bearings
    Straight1 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 1))
    Straight2 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 2))
    Straight3 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 3))
    Straight4 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 4))
    Straight5 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 5))

    # Bank bearings
    LeftBank1 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Left, 1))
    LeftBank2 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Left, 2))
    LeftBank3 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Left, 3))
    
    RightBank1 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Right, 1))
    RightBank2 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Right, 2))
    RightBank3 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Right, 3))

    # Turn bearings
    LeftTurn1 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Left, 1))
    LeftTurn2 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Left, 2))
    LeftTurn3 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Left, 3))
    
    RightTurn1 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Right, 1))
    RightTurn2 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Right, 2))
    RightTurn3 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Right, 3))

    # Koiogren Turn bearings
    KTurn1 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 1), 180)
    KTurn2 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 2), 180)
    KTurn3 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 3), 180)
    KTurn4 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 4), 180)
    KTurn5 = Bearing(MovementTemplate(MovementTemplate.Type.Straight, MovementTemplate.Direction.Straight, 5), 180)

    # Segnor's Loop bearings
    LeftSLoop1 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Left, 1), 180)
    LeftSLoop2 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Left, 2), 180)
    LeftSLoop3 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Left, 3), 180)

    RightSLoop1 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Right, 1), 180)
    RightSLoop2 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Right, 2), 180)
    RightSLoop3 = Bearing(MovementTemplate(MovementTemplate.Type.Bank, MovementTemplate.Direction.Right, 3), 180)
    
    # Tallon Roll bearings (fol-de-rol)
    # TODO: you're actually allowed to do some additional translation along the edge of the base after a TRoll...
    TRoll1 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Left, 1), -90)
    TRoll2 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Left, 2), -90)
    TRoll3 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Left, 3), -90)
    
    RightTRoll1 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Right, 1), 90)
    RightTRoll2 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Right, 2), 90)
    RightTRoll3 = Bearing(MovementTemplate(MovementTemplate.Type.Turn, MovementTemplate.Direction.Right, 3), 90)

    @staticmethod
    def bearing_from_string(bearing_name):
        """
        Get a bearing from its string name
        """
        for bearing in BearingRegistry:
            if bearing.name == bearing_name:
                return bearing

        raise ValueError("Unknown bearing: {0}".format(bearing_name))