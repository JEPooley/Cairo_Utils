import cairo

from shapes import Shapes

class Canvas:

    def __init__(self, width: int, height: int):
        self._ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self._cr = cairo.Context(self.ims)
        self._width = width
        self._height = height

    @property
    def cr(self):
        return self._cr

    @property
    def ims(self):
        return self._ims

    def background_fill(self, rgba):
        Shapes.draw_rectangle(self.cr, 0, 0, self._width, self._height, rgba)