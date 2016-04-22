from models.faction import Faction
from models.tie_fighter import TieFighter
from models.x_wing import XWing

import cairo
import math
import os

class ShipRenderer:
    """
    Renderer for drawing ship pilot tokens
    """
    def __init__(self, ship):
        """
        Constructor
        ship: The ship to render
        """
        # Load the token image
        current_dir = os.path.dirname(os.path.abspath(__file__))
        pilot_token_image = self._get_pilot_token_image(ship)
        pilot_token_surface = cairo.ImageSurface.create_from_png(os.path.join(current_dir, pilot_token_image))

        # Compute the pattern scaling
        sw, sh = pilot_token_surface.get_width(), pilot_token_surface.get_height()
        bw, bh = ship.base_size

        # Set members
        self._ship = ship
        self._base_color_rgba = self._get_base_color()
        self._pilot_token_surface_pattern = cairo.SurfacePattern(pilot_token_surface)
        self._pilot_token_surface_pattern.set_matrix(cairo.Matrix(xx=sw/bw, yy=sh/bh, x0=sw/2, y0=sh/2))
        
    def render(self, context):
        """
        Render this ship
        context: The Cairo context to render to
        """
        context.save()

        # Get the ship's base size and position
        w, h = self._ship.base_size
        x, y = self._ship.position

        # Move to the ship's position on the board
        context.translate(x, y)
        context.rotate(math.radians(self._ship.orientation))
        context.rectangle(-w/2, -h/2, w, h)
        context.set_source_rgba(*self._base_color_rgba)
        context.fill()
        context.rectangle(-w/2, -h/2, w, h)
        context.set_source(self._pilot_token_surface_pattern)
        context.fill()
        context.restore()
        
    def _get_base_color(self):
        """
        Get the base color from the ship's faction
        """
        if self._ship.faction == Faction.rebel:
            return (1, 0, 0, 1)
        elif self._ship.faction == Faction.imperial:
            return (0, 1, 0, 1)
        elif self._ship.faction == Faction.scum:
            return (1, 1, 0, 1)
        else:
            raise ValueError("Unexpected faction: {0}".format(self._ship.faction))

    def _get_pilot_token_image(self, ship):
        """
        Get the pilot token image for a given ship
        ship: The ship to get the pilot token image for
        """
        if isinstance(ship, XWing):
            return "../images/x_wing_pilot_token.png"
        elif isinstance(ship, TieFighter):
            return "../images/tie_fighter_pilot_token.png"
        else:
            raise ValueError("Unknown ship type")