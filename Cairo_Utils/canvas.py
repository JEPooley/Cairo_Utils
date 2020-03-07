import cairo as cr

from Cairo_Utils.shapes import Shapes
from Cairo_Utils.colour import Colour

class Canvas(Shapes, Colour):

    def __init__(self, width: int, height: int):
        self._ims = cr.ImageSurface(cr.FORMAT_ARGB32, width, height)
        self._ctx = cr.Context(self._ims)
        self._width = width
        self._height = height
        Shapes.__init__(self, self._ctx)
        Colour.__init__(self, self._ctx)

    def background_fill(self, rgba):
        self.rectangle(0, 0, self._width, self._height)
        self.fill(rgba)

    def save_as_png(self, path):
        self._ims.write_to_png(path)

if __name__ == '__main__':
    c = Canvas(1000, 1000)

    c.background_fill((.2, .8, .2))

    c.circle(500, 500, 100)
    c.fill((0.4, 0., 0.1))
    c.circle(500, 500, 200)
    c.stroke(20, (200, 20, 90))
    c.save_as_png('test.png')