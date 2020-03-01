import cairo
import math

from Cairo_Utils.colour import Colour

class Shapes:

    @classmethod
    def draw_rectangle(cls, cr: cairo.Context, x: float, y: float,
                       width: float, height: float, rgba: tuple):
        cr.set_source_rgba(*Colour.unpack_rgba(rgba))
        cr.rectangle(x, y, width, height)
        cr.fill()

    @classmethod
    def draw_circle_fill(cls, cr: cairo.Context, x: float, y: float,
                         radius: float, rgba: tuple):
        cr.set_source_rgba(*Colour.unpack_rgba(rgba))
        cr.arc(x, y, radius, 0, 2 * math.pi)
        cr.fill()

    @classmethod
    def draw_circle_fill_shade(cls, cr: cairo.Context, x: float, y: float,
                               radius: float, shift: float, rgba: tuple):
        cls.draw_circle_fill(cr, x, y, radius, rgba)
        cls.draw_circle_fill(cr, x - shift, y - shift, radius, (0, 0, 0, 0.1))


if __name__ == '__main__':
    from canvas import Canvas

    WIDTH = 3000
    HEIGHT = 2000

    # Create Canvas
    canvas = Canvas(WIDTH, HEIGHT)
    cr = canvas.cr
    ims = canvas.ims
    canvas.background_fill((.2, .2, .2, 0.5))

    # Draw shapes
    Shapes.draw_circle_fill(cr, WIDTH / 2, HEIGHT / 2, 200, (1, 0.5, 0.1))

    ims.write_to_png('test.png')
