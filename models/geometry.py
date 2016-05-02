import math
import numpy as np

from shapely.affinity import translate
from shapely.geometry import Polygon, polygon

# 100mm for range 1
RANGE_ONE = 100

def get_arc_footprint(ship, weapon):
    """
    Get a shape representing the arc footprint from the base shape, up to AT LEAST range 3 (maybe more)
    ship: The ship to measure arc from
    weapon: The weapon to measure arc of
    return: The geometric object representing arc footprint from the base shape
    """
    theta = ship.orientation + weapon.firing_direction
    start_angle = theta - weapon.firing_arc / 2
    end_angle = theta + weapon.firing_arc / 2
    angle_step = 1 # degree
    bx, by = ship.base_size

    # To be at least range 3, we need to add at least the centre-to-corner distance for the base template
    min_dist_from_centre = 0.5 * math.sqrt(bx * bx + by * by)
    dist = min_dist_from_centre + RANGE_ONE * 3

    # Generate sector over the angle range
    angles = np.radians(np.linspace(start_angle, end_angle, (end_angle - start_angle) / angle_step))
    points = [(0, 0)] + list(zip(np.sin(angles) * dist, np.cos(angles) * dist))
    sector = polygon.orient(Polygon(points))

    # Translate the result to be centred on the ship
    return translate(sector, ship.position[0], ship.position[1])

def get_range_footprint(base_shape, range_steps):
    """
    Get a shape representing the range footprint from the base shape
    base_shape: A Shapely polygon representing the base shape to get range from
    range_steps: The list of ranges to allow, in ascending order, e.g. [1, 2, 3]
    return: The geometric object representing range footprint from the base shape
    """
    # Build contiguous ranges to consider
    # If range steps are [1, 3] there are two discontinuous ranges.
    # In every other case, it's simply a single object
    if range_steps == [1, 3]:
        bounds_list = [[0, 1], [2, 3]]
    else:
        bounds_list = [[range_steps[0] - 1, range_steps[-1]]]

    total_footprint = None
    for bounds in bounds_list:
        # Build the (potentially holey) footprint for this range group
        footprint = base_shape.buffer(RANGE_ONE * bounds[1])
        if bounds[0] > 0:
            inner_footprint = base_shape.buffer(RANGE_ONE * bounds[0])
            footprint = footprint.difference(inner_footprint)

        # Union if we're in a two-disjoint-ranges scenario (e.g. [1, 3])
        if total_footprint == None:
            total_footprint = footprint
        else:
            total_footprint = total_footprint.union(footprint)

    return total_footprint
