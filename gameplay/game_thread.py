from gameplay.setup import Setup
from gameplay.turn import Turn

import threading

class GameThread:
    """
    The game thread that drives the turn sequence
    """
    def __init__(self, game):
        """
        Constructor
        game: The game to run
        """
        self._game = game
        self._stop = False

        # Start the thread
        self._thread = threading.Thread(target=self._thread_body)
        self._thread.start()

    def join(self):
        """
        Wait for the game thread to complete
        """
        self._stop = True
        self._thread.join()

    def _thread_body(self):
        """
        Thread body for the game thread
        """
        # Set up the board
        setup_phase = Setup(self._game)
        setup_phase.execute()

        # While both players are alive, execute turns
        while (not self._stop) and not self._game.is_over():
            turn = Turn(self._game)
            turn.execute()
