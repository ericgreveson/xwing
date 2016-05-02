import cairo
import math
import os

class FootprintRenderer:
    """
    Renderer for drawing pilot tokens
    """
    def __init__(self, footprint):
        """
        Constructor
        footprint: The footprint geometry to render
        """
        self._footprint = footprint
        self._fill_color = (1, 1, 0, 0.4)
        self._stroke_color = (1, 1, 0, 0.9)
        
    def render(self, context):
        """
        Render this ship
        context: The Cairo context to render to
        """
        context.save()

        # The 
        # Move to the first point on the polygon
        x, y = self._footprint.boundary.coords[0]
        context.move_to(x, y)

        # Draw the boundary
        for x, y in self._footprint.boundary.coords[1:-1]:
            context.line_to(x, y)

        # Close, fill and stroke this path
        context.close_path()
        context.set_source_rgba(*self._fill_color)
        context.fill_preserve()
        context.set_source_rgba(*self._stroke_color)
        context.stroke()
        context.restore()

    def _get_pilot_token_image(self, pilot):
        """
        Get the pilot token image for a given pilot
        pilot: The pilot to get the pilot token image for
        """
        script_path = os.path.dirname(os.path.abspath(__file__))
        image_file = os.path.join(script_path, "..", "images", "{0}_pilot_token.png".format(pilot.name))
        if not os.path.exists(image_file):
            raise ValueError("No pilot token image: {0}".format(image_file))

        return image_file