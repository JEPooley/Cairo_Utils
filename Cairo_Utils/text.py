from typing import Union

import cairo as cr

import Cairo_Utils.colour as clr


class Text:

    def __init__(self, ctx: cr.Context, font_family: str = 'sans-serif',
                 font_slant: str = 'normal',
                 font_weight: str = 'normal',
                 colour: Union[tuple, str] = (0, 0, 0)):
        self._ctx = ctx
        self.font_family = font_family
        self.font_slant = font_slant
        self.font_weight = font_weight
        self.colour = colour

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        self._colour = clr.colour(value)

    @property
    def font_slant(self):
        return self._font_slant

    @font_slant.setter
    def font_slant(self, value):
        if value.lower() == 'italic':
            self._font_slant = cr.FONT_SLANT_ITALIC
        else:
            self._font_slant = cr.FONT_SLANT_NORMAL
        try:
            self._update_font()
        except AttributeError:
            pass

    @property
    def font_weight(self):
        return self._font_weight

    @font_weight.setter
    def font_weight(self, value):
        if value.lower() == 'bold':
            self._font_weight = cr.FONT_WEIGHT_BOLD
        else:
            self._font_weight = cr.FONT_WEIGHT_NORMAL
        try:
            self._update_font()
        except AttributeError:
            pass

    def _update_font(self):
        self._ctx.select_font_face(self.font_family,
                                   self.font_slant,
                                   self.font_weight)

    def set_font(self, colour: Union[tuple, str] = (0, 0, 0),
                 font_family: str = 'sans-serif',
                 font_slant: str = 'normal',
                 font_weight: str = 'normal'):
        self.colour = colour
        self.font_family = font_family
        self.font_slant = font_slant
        self.font_weight = font_weight

    def add_text(self, text: str, x: float, y: float,
                 font_size: float, top_right: bool = False):
        self._ctx.set_source_rgba(*self.colour)
        self._ctx.set_font_size(font_size)
        if top_right:
            xx, yy, w, h, dx, dy = self._ctx.text_extents(text)
            self._ctx.move_to(x - w, y + font_size)
        else:
            self._ctx.move_to(x, y + font_size)
        self._ctx.show_text(text)
