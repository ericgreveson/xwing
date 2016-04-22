from models.movement_template import MovementTemplate
from models.tie_fighter import TieFighter
from models.x_wing import XWing

class Board:
    """
    Game board, on which everything else can be placed
    """
    def __init__(self):
        """
        Constructor
        """
        # Board is 3ft by 3ft
        board_size = 914
        self.dimensions = (board_size, board_size)

        # Add a TIE fighter in the bottom left corner
        imperial_one = TieFighter()
        imperial_one.position = (MovementTemplate.STANDARD_WIDTH * 2, MovementTemplate.STANDARD_WIDTH * 2)
        imperial_one.orientation = 180

        imperial_two = TieFighter()
        imperial_two.position = (MovementTemplate.STANDARD_WIDTH * 5, MovementTemplate.STANDARD_WIDTH * 2)
        imperial_two.orientation = 180

        rebel_one = XWing()
        rebel_one.position = (board_size - MovementTemplate.STANDARD_WIDTH * 2, board_size - MovementTemplate.STANDARD_WIDTH * 2)
        rebel_one.orientation = 0

        self.ships = [imperial_one, imperial_two, rebel_one]