import math


class Shapes:

    def __init__(self, ctx):
        self._ctx = ctx

    def rectangle(self, x, y, width, height):
        self._ctx.rectangle(x, y, width, height)

    def circle(self, x, y, radius):
        self._ctx.arc(x, y, radius, 0, 2 * math.pi)

    def crescent(self, x, y, radius, shift, rotate=0.0):
        phi = math.acos(shift / (2 * radius))
        x_shift, y_shift = shift * math.cos(rotate), shift * math.sin(rotate)
        x, y = x + x_shift, y + y_shift
        self._ctx.arc(x, y, radius, rotate + math.pi - phi,
                     rotate + phi - math.pi)
        self._ctx.arc_negative(x - x_shift, y - y_shift, radius,
                              rotate - phi, rotate + phi)
        self._ctx.close_path()


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
    Shapes.draw_gradient_sphere(ctx, WIDTH/2, HEIGHT/2,
                                200, 100, (1, 0.2, 0.4))

    ims.write_to_png('test.png')
