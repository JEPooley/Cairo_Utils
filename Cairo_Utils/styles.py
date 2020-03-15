from typing import Union

import cairo as cr

import Cairo_Utils.colour as clr


class StrokeStyles:
    '''Draw line or shape outline onto an image surface
    '''

    def __init__(self, ctx: cr.Context):
        self._ctx = ctx

    def stroke(self,
               linewidth: float,
               colour: Union[tuple, str],
               join_type: str = 'miter',
               cap_type: str = 'square'):
        '''Draw line or shape outline onto an image surface
           Note: use after a shape/line drawing command
        '''
        colour = clr.colour(colour)
        self._ctx.set_source_rgba(*colour)
        self._ctx.set_line_width(linewidth)
        self.set_join(join_type)
        self.set_cap(cap_type)
        self._ctx.stroke()

    def set_join(self, join_type: str):
        '''Set line joins to be rounded ('round'), bevelled ('bevel')
           or mitered ('miter')
        '''
        if join_type == 'miter':
            self._ctx.set_line_join(cr.LINE_JOIN_MITER)
        elif join_type == 'round':
            self._ctx.set_line_join(cr.LINE_JOIN_ROUND)
        elif join_type == 'bevel':
            self._ctx.set_line_join(cr.LINE_JOIN_BEVEL)
        else:
            raise ValueError(f'stroke join type "{join_type}" not understood')

    def set_cap(self, cap_type: str):
        '''Set line ends to be extended square ('square'), rounded ('round')
           or flush square ('butt')
        '''
        if cap_type == 'square':
            self._ctx.set_line_cap(cr.LINE_CAP_SQUARE)
        elif cap_type == 'round':
            self._ctx.set_line_cap(cr.LINE_CAP_ROUND)
        elif cap_type == 'butt':
            self._ctx.set_line_cap(cr.LINE_CAP_BUTT)
        else:
            raise ValueError(f'stroke cap type "{cap_type}" not understood')


class FillStyles:
    '''Draw filled shape onto an image surface
    '''

    def __init__(self, ctx: cr.Context):
        self._ctx = ctx

    def fill(self, colour: Union[tuple, str]):
        '''Draw filled shape onto an image surface
           Note: use after a shape/line drawing command
        '''
        colour = clr.colour(colour)
        self._ctx.set_source_rgba(*colour)
        self._ctx.fill()
