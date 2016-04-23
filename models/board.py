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
        self.pilots = []