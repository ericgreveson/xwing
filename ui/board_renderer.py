from ui.footprint_renderer import FootprintRenderer
from ui.pilot_renderer import PilotRenderer

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
        
        self._footprint_renderers = []
        self._pilot_renderers = []
        self._refresh_sub_renderers()

    def render(self, context):
        """
        Render the board
        context: The Cairo context to render to
        """
        self._refresh_sub_renderers()

        context.save()

        # Draw the board
        context.save()
        context.scale(1.0 / self._board_surface.get_width(), 1.0 / self._board_surface.get_height())
        context.rectangle(0, 0, 1, 1)
        context.set_source_surface(self._board_surface)
        context.paint()
        context.restore()

        # Draw any sub-renderers
        # Place the origin in the bottom left corner
        w, h = self._board.dimensions
        context.translate(0, 1)
        context.scale(1.0 / w, -1.0 / h)
        for sub_renderer in self._footprint_renderers + self._pilot_renderers:
            sub_renderer.render(context)

        context.restore()

    def _refresh_sub_renderers(self):
        """
        Recreate sub-renderers, e.g. if the board contents have changed
        """
        self._footprint_renderers = [FootprintRenderer(footprint) for footprint in self._board.footprints]
        if len(self._pilot_renderers) != len(self._board.pilots):
            self._pilot_renderers = [PilotRenderer(pilot) for pilot in self._board.pilots]
