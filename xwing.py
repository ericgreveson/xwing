from gameplay.game_thread import GameThread
from gameplay.console_player import ConsolePlayer
from models.board import Board
from models.faction import Faction
from models.game import Game
from models.pilot_registry import PilotRegistry
from models.ship_registry import ShipRegistry
from ui.main_window import MainWindow

import os
import sys
import tkinter as tk

def main(argv):
    """
    Program entry point
    argv: Command line args (excluding the script name)
    """
    # Load the ship registry
    script_path = os.path.dirname(os.path.abspath(__file__))
    ships_json = os.path.join(script_path, "data", "ship_registry.json")
    ship_registry = ShipRegistry(ships_json)

    # Load the pilot registry
    pilots_json = os.path.join(script_path, "data", "pilot_registry.json")
    pilot_registry = PilotRegistry(pilots_json, ship_registry)

    # Create the board
    board = Board()

    # Create players for each side
    player1 = ConsolePlayer(Faction.imperial, board)
    player2 = ConsolePlayer(Faction.rebel, board)

    # Wrap these all up in the game object
    game = Game(board, [player1, player2], pilot_registry)

    # Create the game thread and set it running
    game_thread = GameThread(game)

    # Build the UI and set it running
    root = tk.Tk()
    app = MainWindow(board, master=root)
    try:
        app.mainloop()
    except KeyboardInterrupt:
        pass

    # Once the main window is closed, join the game thread
    game_thread.join()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])