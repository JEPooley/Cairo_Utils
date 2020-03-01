import math

import cairo as cr

from Cairo_Utils.colour import Colour


class Shapes:

    @classmethod
    def draw_rectangle(cls, ctx, x, y,
                       width, height, rgba):
        ctx.set_source_rgba(*Colour.unpack_rgba(rgba))
        ctx.rectangle(x, y, width, height)
        ctx.fill()

    @classmethod
    def draw_circle_fill(cls, ctx, x, y,
                         radius, rgba):
        ctx.set_source_rgba(*Colour.unpack_rgba(rgba))
        ctx.arc(x, y, radius, 0, 2 * math.pi)
        ctx.fill()

    @classmethod
    def draw_circle_fill_shade(cls, ctx, x, y,
                               radius, shift, rgba, rotate=0.0):
        x_shift, y_shift = shift * math.cos(rotate), shift * math.sin(rotate)
        cls.draw_circle_fill(ctx, x - x_shift, y - y_shift, radius, (0, 0, 0, 0.3))
        cls.draw_circle_fill(ctx, x, y, radius, rgba)

    @classmethod
    def draw_crescent(cls, ctx, x, y,
                      radius, shift, rgba,
                      rotate=0.0):
        # Angle and Shift
        phi = math.acos(shift / (2 * radius))
        x_shift, y_shift = shift * math.cos(rotate), shift * math.sin(rotate)
        # Draw crescent
        x, y = x + x_shift, y + y_shift
        ctx.arc(x, y, radius, rotate + math.pi - phi, rotate + phi - math.pi)
        ctx.arc_negative(x - x_shift, y - y_shift, radius,
                         rotate - phi, rotate + phi)
        # Fill
        ctx.close_path()
        ctx.set_source_rgba(*Colour.unpack_rgba(rgba))
        ctx.fill()

    @classmethod
    def draw_sphere(cls, ctx, x, y, radius, shift, rgba, rotate=0):
        cls.draw_circle_fill_shade(ctx, x, y, radius, shift, rgba, rotate)
        cls.draw_crescent(ctx, x, y, radius * 0.94, shift, (0, 0, 0, 0.2), rotate)

if __name__ == '__main__':
    from canvas import Canvas

    WIDTH = 3000
    HEIGHT = 2000

    # Create Canvas
    canvas = Canvas(WIDTH, HEIGHT)
    ctx = canvas.ctx
    ims = canvas.ims
    canvas.background_fill((.3, .3, .3))

    # Draw shapes
    Shapes.draw_sphere(ctx, WIDTH / 2, HEIGHT / 2, 200, 50, (1, 0.5, 0.1))

    ims.write_to_png('test.png')
