class Bearing:
    """
    A bearing consists of a movement template together with any extra rotation
    """
    def __init__(self, template, extra_rotation=0):
        """
        Constructor
        template: The movement template to use
        extra_rotation: Any extra rotation angle, in degrees, to apply after the movement template
        """
        self.template = template
        self.extra_rotation = extra_rotation