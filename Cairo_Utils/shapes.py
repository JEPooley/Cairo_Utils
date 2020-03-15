import math

import cairo as cr
from typing import List


class Shapes:

    def __init__(self, ctx: cr.Context):
        self._ctx = ctx

    def rectangle(self, x: float, y: float,
                  width: float, height: float):
        self._ctx.rectangle(x, y, width, height)

    def circle(self, x: float, y: float,
               radius: float):
        self._ctx.arc(x, y, radius, 0, 2 * math.pi)

    def line(self, coord_list: List[tuple]):
        self._ctx.move_to(*coord_list[0])
        [self._ctx.line_to(*coord) for coord in coord_list[1:]]

    def polygon(self, coord_list: List[tuple]):
        self.line(coord_list)
        self._ctx.close_path()

    def crescent(self, x: float, y: float,
                 radius: float, shift: float,
                 rotate: float = 0.0):
        phi = math.acos(shift / (2 * radius))
        x_shift, y_shift = shift * math.cos(rotate), shift * math.sin(rotate)
        self._ctx.arc(x + x_shift, y + y_shift, radius, rotate + math.pi - phi,
                     rotate + phi - math.pi)
        self._ctx.arc_negative(x, y, radius,
                              rotate - phi, rotate + phi)
        self._ctx.close_path()
