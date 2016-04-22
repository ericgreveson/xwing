from ui.ship_renderer import ShipRenderer

import cairo
import os

BOARD_IMAGE = "../images/death_star_mat.png"

class BoardRenderer:
    """
    Renderer for the board
    """
    def __init__(self, board):
        """
        Constructor
        board: The board model to render
        """
        self._board = board

        # Load the board background image
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self._board_surface = cairo.ImageSurface.create_from_png(os.path.join(current_dir, BOARD_IMAGE))

        # Create sub-renderers
        self._sub_renderers = []
        for ship in self._board.ships:
            self._sub_renderers.append(ShipRenderer(ship))

    def render(self, context):
        """
        Render the board
        context: The Cairo context to render to
        """
        context.save()

        # Draw the board
        context.save()
        context.scale(1.0 / self._board_surface.get_width(), 1.0 / self._board_surface.get_height())
        context.rectangle(0, 0, 1, 1)
        context.set_source_surface(self._board_surface)
        context.paint()
        context.restore()

        # Draw any sub-renderers
        w, h = self._board.dimensions
        context.scale(1.0 / w, 1.0 / h)
        for sub_renderer in self._sub_renderers:
            sub_renderer.render(context)

        context.restore()