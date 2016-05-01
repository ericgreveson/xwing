from random import randint

class GreenDie:
    """
    Defence die, 8 sides in total:
    3 blank
    2 focus
    3 evade
    """
    BLANK = "blank"
    FOCUS = "focus"
    EVADE = "evade"

    @staticmethod
    def roll():
        """
        Roll a green die
        return: the result (BLANK, FOCUS etc)
        """
        face_rolled = randint(0, 7)
        if face_rolled <= 2:
            return GreenDie.BLANK
        elif face_rolled <= 4:
            return GreenDie.FOCUS
        else:
            return GreenDie.EVADE
