from models.bearing_registry import BearingRegistry
from models.faction import Faction
from models.maneuver import Maneuver

from ui.board_renderer import BoardRenderer

import cairo
import tkinter as tk

from PIL import Image, ImageTk

class MainWindow(tk.Frame):
    """
    Application main window
    board: Game board to represent
    master: Parent widget
    """
    def __init__(self, board, master=None):
        """
        Constructor
        board: Game board to display
        master: parent Tk object
        width: Width, in pixels, of the window
        height: Height, in pixels, of the window
        """
        super().__init__(master)
        self.pack()

        self._board = board

        # Create Tk label for image display
        self._label = tk.Label(self)
        self._label.pack(expand=True, fill="both")

        # Create the board renderer
        self._board_renderer = BoardRenderer(self._board)

        # Do the initial draw
        self._bearings = [
            BearingRegistry.Straight1,
            BearingRegistry.LeftBank1,
            BearingRegistry.Straight2,
            BearingRegistry.RightBank1,
            None,
            BearingRegistry.LeftTurn3,
            None,
            BearingRegistry.RightTurn2,
            None,
            BearingRegistry.Straight3,
            BearingRegistry.LeftSLoop2,
            BearingRegistry.KTurn4]
        self._bearings.reverse()
        self._redraw_callback()

    def _redraw_callback(self):
        """
        Redraw the window
        """
        # Move the first ship
        if self._bearings:
            bearing = self._bearings.pop()
            if bearing:
                first_imperial = [ship for ship in self._board.ships if ship.faction == Faction.imperial][0]
                movement = Maneuver(bearing.value)
                movement.apply(first_imperial)

        # Create or update rendering surface
        edge_size = 720
        self._update_surface(edge_size)

        # Draw on the surface
        self._board_renderer.render(self._context)

        # Transfer the surface pixels to the window
        surface_bytes = self._surface.get_data().tobytes()
        self._wrapped_image = ImageTk.PhotoImage(Image.frombytes("RGBA", (edge_size, edge_size), surface_bytes, "raw", "BGRA", 0, 1))
        self._label["image"] = self._wrapped_image
        
        # Repeat ad infinitum
        self.after(500, self._redraw_callback)

    def _update_surface(self, edge_size):
        """
        Create (or recreate) the rendering surface if size has changed
        edge_size: The width / height of the surface
        """
        # We want a square surface
        if (not hasattr(self, "_surface")) or (self._surface.get_width() != edge_size):
            self._surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, edge_size, edge_size)
            self._context = cairo.Context(self._surface)
            self._context.scale(edge_size, edge_size)