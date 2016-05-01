from random import randint

class RedDie:
    """
    Attack die, 8 sides in total:
    2 blank
    2 focus
    3 damage
    1 crit
    """
    BLANK = "blank"
    FOCUS = "focus"
    DAMAGE = "damage"
    CRIT = "crit"

    @staticmethod
    def roll():
        """
        Roll a red die
        return: the result (BLANK, FOCUS etc)
        """
        face_rolled = randint(0, 7)
        if face_rolled <= 1:
            return RedDie.BLANK
        elif face_rolled <= 3:
            return RedDie.FOCUS
        elif face_rolled <= 6:
            return RedDie.DAMAGE
        else:
            return RedDie.CRIT
