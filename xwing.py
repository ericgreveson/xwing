from models.board import Board
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

    # Create the board
    board = Board()
    board.load_board_setup(argv[0])

    # Build the UI 
    root = tk.Tk()
    app = MainWindow(board, master=root)
    app.mainloop()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])