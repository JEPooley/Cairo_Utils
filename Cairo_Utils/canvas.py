import cairo as cr

from Cairo_Utils.shapes import Shapes

class Canvas:

    def __init__(self, width: int, height: int):
        self._ims = cr.ImageSurface(cr.FORMAT_ARGB32, width, height)
        self._ctx = cr.Context(self.ims)
        self._width = width
        self._height = height

    @property
    def ctx(self):
        return self._ctx

    @property
    def ims(self):
        return self._ims

    def background_fill(self, rgba):
        Shapes.draw_rectangle(self.ctx, 0, 0, self._width, self._height, rgba)