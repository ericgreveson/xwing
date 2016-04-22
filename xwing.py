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
    root = tk.Tk()
    board = Board()
    app = MainWindow(board, master=root)
    app.mainloop()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])