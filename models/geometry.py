# 100mm for range 1
RANGE_ONE = 100

def get_range_footprint(base_shape, range_steps):
    """
    Get a shape representing the range footprint of the base shape
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
