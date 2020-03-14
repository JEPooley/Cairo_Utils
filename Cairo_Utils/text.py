import cairo as cr

import Cairo_Utils.colour as clr


class Text:

    def __init__(self, ctx, font_family='sans-serif', font_slant='normal',
                 font_weight='normal', colour=(0, 0, 0)):
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

    def set_font(self, colour=(0,0,0), font_family='sans-serif', font_slant='normal',
                    font_weight='normal'):
        self.colour = colour
        self.font_family = font_family
        self.font_slant = font_slant
        self.font_weight = font_weight

    def add_text(self, text, x, y, font_size):
        self._ctx.set_source_rgba(*self.colour)
        self._ctx.set_font_size(font_size)
        self._ctx.move_to(x, y)
        self._ctx.show_text(text)
