import math
import numpy as np

class Maneuver:
    """
    Apply a bearing to move a ship
    """
    def __init__(self, bearing):
        """
        Constructor
        bearing: The bearing to use for this maneuver
        """
        self._bearing = bearing
        
    def apply(self, ship):
        """
        Apply this maneuver to the given ship
        """
        # Unpack bearing bits
        template = self._bearing.template

        # Translate the ship
        ship_dir = Maneuver._direction_vector(ship.orientation)
        start_point = np.asarray(ship.position) + ship_dir * ship.base_size[1] / 2
        template_delta = Maneuver._rotation_matrix(ship.orientation) @ template.arc_endpoint()
        end_point = start_point + template_delta
        new_ship_midpoint = end_point + Maneuver._direction_vector(ship.orientation + template.rotation_angle()) * ship.base_size[1] / 2
        ship.position = list(new_ship_midpoint)

        # Rotate the ship
        ship.orientation += template.rotation_angle() + self._bearing.extra_rotation
        ship.orientation = Maneuver._wrap_angle_range(ship.orientation)

    @staticmethod
    def _direction_vector(angle):
        """
        Get a direction vector for the given angle
        angle: Angle in degrees (0 degrees indicates direction of (0, 1))
        return: 2D numpy array with unit vector
        """
        theta = math.radians(angle)
        return np.asarray([-math.sin(theta), math.cos(theta)])

    @staticmethod
    def _rotation_matrix(angle):
        """
        Get a rotation matrix for the given angle
        angle: Angle in degrees
        return: 2x2 numpy array containing 2D rotation matrix
        """
        theta = math.radians(angle)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        return np.asarray([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

    @staticmethod
    def _wrap_angle_range(angle):
        """
        Ensure the angle is in the range [0, 360)
        angle: Angle in degrees
        return: Angle wrapped to range [0, 360)
        """
        while angle >= 360:
            angle -= 360
        while angle < 0:
            angle += 360
        return angle