from typing import Union

import cairo as cr
import colour as clr


class StrokeStyles:

    def __init__(self, ctx):
        self._ctx = ctx

    def stroke(self,
               linewidth: float,
               colour: Union[tuple, str],
               join_type: str = 'miter',
               cap_type: str = 'square'):

        colour = clr.colour(colour)
        self._ctx.set_source_rgba(*colour)
        self._ctx.set_line_width(linewidth)
        self.set_join(join_type)
        self.set_cap(cap_type)
        self._ctx.stroke()

    def set_join(self, join_type):
        if join_type == 'miter':
            self._ctx.set_line_join(cr.LINE_JOIN_MITER)
        elif join_type == 'round':
            self._ctx.set_line_join(cr.LINE_JOIN_ROUND)
        elif join_type == 'bevel':
            self._ctx.set_line_join(cr.LINE_JOIN_BEVEL)
        else:
            raise ValueError(f'stroke join type "{join_type}" not understood')

    def set_cap(self, cap_type):
        if cap_type == 'square':
            self._ctx.set_line_cap(cr.LINE_CAP_SQUARE)
        elif cap_type == 'round':
            self._ctx.set_line_cap(cr.LINE_CAP_ROUND)
        elif cap_type == 'butt':
            self._ctx.set_line_cap(cr.LINE_CAP_BUTT)
        else:
            raise ValueError(f'stroke cap type "{cap_type}" not understood')


class FillStyles:

    def __init__(self, ctx):
        self._ctx = ctx

    def fill(self, colour: Union[tuple, str]):
        colour = clr.colour(colour)
        self._ctx.set_source_rgba(*colour)
        self._ctx.fill()
