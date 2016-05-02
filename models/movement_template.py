import math
import numpy as np

from enum import Enum

class MovementTemplate:
    """
    Represents a movement template
    """
    # A "1 forward" template is 20mm wide by 40mm long
    STANDARD_LENGTH = 40
    
    TURN_RADII = {
        1: 35,
        2: 63,
        3: 90
        }

    BANK_RADII = {
        1: 80,
        2: 130,
        3: 180
        }

    class Direction(Enum):
        Left = -1
        Straight = 0
        Right = 1

    class Type(Enum):
        Straight = 0
        Bank = 45
        Turn = 90

    def __init__(self, type, direction, length):
        """
        Constructor
        type: The MovementTemplate.Type
        direction: The MovementTemplate.Direction
        length: number in range 1 to 5
        """
        self._type = type
        self._direction = direction
        self._length = length

    def rotation_angle(self):
        """
        Get the rotation angle from the start of this template to the end
        """
        return self._direction.value * self._type.value

    def arc_endpoint(self):
        """
        Get the endpoint of the movement for this template assuming it's applied along +Y axis
        return: 2D numpy array containing endpoint relative to (0, 0)
        """
        # Apply the appropriate template (assuming a right turn here)
        type = self._type
        if type == MovementTemplate.Type.Turn:
            radius = MovementTemplate.TURN_RADII[self._length]
            ep = radius * np.asarray([1, -1])
        elif type == MovementTemplate.Type.Bank:
            radius = MovementTemplate.BANK_RADII[self._length]
            sqrt_half = math.sqrt(0.5)
            ep = radius * np.asarray([1 - sqrt_half, sqrt_half])
        elif type == MovementTemplate.Type.Straight:
            ep = np.asarray([0, self._length * MovementTemplate.STANDARD_LENGTH])
        else:
            raise ValueError("Invalid direction")
        
        # We can treat left turns as reflections of right turns in the Y axis
        ep[0] *= self._direction.value

        return ep
