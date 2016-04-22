import math
import numpy as np

from enum import Enum

class MovementTemplate:
    """
    Represents a movement template
    """
    # A "1 forward" template is 20mm wide by 40mm long
    STANDARD_WIDTH = 20
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
        LeftTurn = -90
        LeftBank = -45
        Straight = 0
        RightBank = 45
        RightTurn = 90

    def __init__(self, direction, length):
        """
        Constructor
        direction: The MovementTemplate.Direction
        length: number in range 1 to 5
        """
        self._direction = direction
        self._length = length

    def apply(self, ship):
        """
        Apply this movement template to the given ship
        """
        # Translate the ship
        ship_dir = self._direction_vector(ship.orientation)
        start_point = np.asarray(ship.position) + ship_dir * ship.base_size[1] / 2
        template_delta = self._arc_endpoint(ship.orientation)
        end_point = start_point + template_delta
        new_ship_midpoint = end_point + self._direction_vector(ship.orientation + self._direction.value) * ship.base_size[1] / 2
        ship.position = list(new_ship_midpoint)

        # Rotate the ship
        ship.orientation += self._direction.value
        if ship.orientation >= 360:
            ship.orientation -= 360
        elif ship.orientation < 0:
            ship.orientation += 360

    def _direction_vector(self, angle):
        """
        Get a direction vector for the given angle
        angle: Angle in degrees (0 degrees indicates direction of (0, 1))
        return: 2D numpy array with unit vector
        """
        theta = math.radians(angle)
        return np.asarray([-math.sin(theta), math.cos(theta)])

    def _arc_endpoint(self, angle):
        """
        Get the endpoint of the movement for this template
        angle: The angle to apply the template at, in degrees
        return: 2D numpy array containing endpoint relative to (0, 0)
        """
        # Rotation matrix to apply to the standard coordinate-system endpoint
        theta = math.radians(angle)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        rotation_matrix = np.asarray([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

        # We can treat right turns as reflections of left turns in the Y axis
        dir = self._direction
        flip_x = False
        if dir == MovementTemplate.Direction.RightTurn:
            dir = MovementTemplate.Direction.LeftTurn
            flip_x = True
        elif dir == MovementTemplate.Direction.RightBank:
            dir = MovementTemplate.Direction.LeftBank
            flip_x = True

        # Apply the appropriate template
        if dir == MovementTemplate.Direction.LeftTurn:
            radius = MovementTemplate.TURN_RADII[self._length]
            ep = radius * np.asarray([1, 1])
        elif dir == MovementTemplate.Direction.LeftBank:
            radius = MovementTemplate.BANK_RADII[self._length]
            sqrt_half = math.sqrt(0.5)
            ep = radius * np.asarray([1 - sqrt_half, sqrt_half])
        elif dir == MovementTemplate.Direction.Straight:
            ep = np.asarray([0, self._length * MovementTemplate.STANDARD_LENGTH])
        else:
            raise ValueError("Invalid direction")

        # If it's a right turn, reflect away
        if flip_x:
            ep[0] = -ep[0]

        return rotation_matrix @ ep
