from models.board import Board
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
    # We expect one arg: the board setup JSON file
    if len(argv) != 1:
        print("Usage: xwing <board_setup.json>")
        return 1

    # Load the ship registry
    registry_json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ship_registry.json")
    ship_registry = ShipRegistry(registry_json_file)

    # Create the board
    board = Board()
    board.load_board_setup(argv[0], ship_registry)

    # Build the UI 
    root = tk.Tk()
    app = MainWindow(board, master=root)
    app.mainloop()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])