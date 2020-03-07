import random

from typing import Tuple


class Colour:

    def __init__(self, ctx):
        self._ctx = ctx

    def fill(self, rgba):
        self._ctx.set_source_rgba(*Colour._unpack_rgba(rgba))
        self._ctx.fill()

    def stroke(self, linewidth, colour):
        colour = self.colour(colour)
        self._ctx.set_source_rgba(*colour)
        self._ctx.set_line_width(linewidth)
        self._ctx.stroke()

    def colour(self, colour):
        colour_type = self.get_colour_type(colour)
        if colour_type == float:
            return self._unpack_rgba(colour)
        elif colour_type == int:
            colour = self.rgb_8bit_to_unit(colour)
            return self._unpack_rgba(colour)
        else:
            colour = self.hex_to_rgba(colour)
            return self._unpack_rgba(colour)

    def random_colour(self, rand_alpha: bool = False) -> Tuple:
        def r(): return random.random()
        if rand_alpha:
            return (r(), r(), r(), r())
        else:
            return (r(), r(), r(), 1)

    @staticmethod
    def _unpack_rgba(rgba: Tuple, alpha=1.) -> Tuple:
        is_a = (len(rgba) == 4)
        if is_a:
            r, g, b, a = rgba
            return r, g, b, a
        else:
            r, g, b = rgba
            return r, g, b, alpha

    @staticmethod
    def get_colour_type(colour):
        if type(colour) == str:
            return str
        elif any([type(c) == float for c in colour]):
            if any([c > 1 for c in colour]):
                raise ValueError('float colours must be between 0 and 1, '
                                  + f'got {colour}')
            return float
        else:
            return int

    @staticmethod
    def rgb_8bit_to_unit(rgb: Tuple) -> Tuple:
        def f(x): return x / 255
        return tuple([f(c) for c in rgb])

    @staticmethod
    def rgb_unit_to_8bit(rgb: Tuple) -> Tuple:
        def f(x): return int(x * 255)
        return tuple([f(c) for c in rgb])

    def hex_to_rgba(self, hex_colour: str) -> Tuple:
        if type(hex_colour) != str:
            raise TypeError('Hex colour expected as string')
        hex_colour = hex_colour.strip('#')
        length = len(hex_colour)
        hex_list = [hex_colour[i: i + 2] for i in range(0, length, 2)]
        rgba = tuple([int(h, 16) for h in hex_list])
        return self.rgb_8bit_to_unit(rgba)

    @staticmethod
    def add_alpha(rgb: Tuple, alpha: float) -> Tuple:
        channels = len(rgb)
        assert channels == 3, f'rgb should be 3-channel, got {channels}\n'\
            + f'>>> {rgb}'
        return rgb + (alpha,)


if __name__ == "__main__":
    hexi = '#2F009F0A'
    unit =  (0, 0.4, 1.0)
    _8bit = (1, 0, 255, 8)
    print(Colour('t').random_colour())
