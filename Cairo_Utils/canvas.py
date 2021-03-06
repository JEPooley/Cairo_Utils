from typing import Union

import cairo as cr

from Cairo_Utils.images import Images
from Cairo_Utils.shapes import Shapes
from Cairo_Utils.styles import FillStyles, StrokeStyles
from Cairo_Utils.text import Text


class Canvas(Shapes, StrokeStyles, FillStyles, Text, Images):
    '''Create and customise an image surface to be drawn on to
    '''

    def __init__(self, width: int, height: int):
        '''Create image surface and initialise drawing tools
        '''
        self._ims = cr.ImageSurface(cr.FORMAT_ARGB32, width, height)
        self._ctx = cr.Context(self._ims)
        self._width = width
        self._height = height
        Shapes.__init__(self, self._ctx)
        StrokeStyles.__init__(self, self._ctx)
        FillStyles.__init__(self, self._ctx)
        Text.__init__(self, self._ctx)
        Images.__init__(self, self._ctx)

    def background_fill(self, colour: Union[tuple, str]):
        '''Set background colour - must be set before drawing
        '''
        self.rectangle(0, 0, self._width, self._height)
        self.fill(colour)

    def frame(self, width: float, colour: Union[tuple, str]):
        '''Adds a frame to the canvas - should be added last for overlay
           effect
        '''
        self.polygon([(0, 0),
                      (self._width, 0),
                      (self._width, self._height),
                      (0, self._height)])
        self.stroke(2 * width, colour)

    def save_as_png(self, path: str):
        '''Save image to PNG format
        '''
        self._ims.write_to_png(path)


if __name__ == '__main__':
    import math
    import numpy as np

    c = Canvas(1000, 1000)

    c.background_fill('#2020DF')

    c.circle(500, 500, 100)
    c.fill((0.4, 0., 0.1))

    c.circle(500, 500, 200)
    c.stroke(20, (200, 20, 90))

    c.rectangle(59, 50, 500, 100)
    c.fill(('#FF9593'))

    c.line([(10, 10),
            (100, 700),
            (300, 100)
            ])
    c.stroke(10, (0, 0, 0), cap_type='round')

    c.crescent(700, 700, 120, 100, math.pi / 3)
    c.stroke(10, (95, 125, 87), join_type='round')

    c.add_image('test.png', 100, 100, 100, 300)

    c.frame(100.2, '#34ABE5')

    x = np.linspace(0, 1000, 100)
    y = 100 * np.sin(x / 100) + 500

    c.line([(xx, yy) for xx, yy in zip(x, y)])
    c.stroke(10, (0, 0, 0))

    c.set_font((0, 1, 0), font_slant='italic', font_weight='bold')
    c.add_text('F(x)', 500, 500, 50, top_right=True)

    c.save_as_png('test.png')
