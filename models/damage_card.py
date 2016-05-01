class DamageCard:
    """
    This represents a damage card, drawn when you run out of shields etc
    """
    def __init__(self):
        """
        Constructor
        """
        self.faceup = False
        self.value = 1

    def flip_faceup(self):
        """
        Flip this damage card faceup
        """
        self.faceup = True