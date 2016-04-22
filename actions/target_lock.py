class TargetLock:
    """
    This represents a Target Lock action
    """
    def __init__(self, max_range=300):
        """
        Constructor
        max_range: The maximum range at which the target lock may be acquired, in mm
        """
        self._max_range = max_range