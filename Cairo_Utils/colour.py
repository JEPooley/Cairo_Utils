import random
import warnings
from typing import Union

import numpy as np


def colour(colour: Union[tuple, str]) -> tuple:
    '''Check input colour and force into rgba [0.0 -> 1.0] format
    '''
    colour_type = get_colour_type(colour)
    if colour_type == float:
        return unpack_rgba(colour)
    elif colour_type == int:
        colour = rgb_8bit_to_unit(colour)
        return unpack_rgba(colour)
    else:
        colour = hex_to_rgba(colour)
        return unpack_rgba(colour)


def random_colour(rand_alpha: bool = False) -> tuple:
    '''Create random rgba colour
    '''
    def r(): return random.random()
    if rand_alpha:
        return (r(), r(), r(), r())
    else:
        return (r(), r(), r(), 1)


def unpack_rgba(rgba: tuple, alpha: float = 1.0) -> tuple:
    '''Add alpha channel to 3-band colours, otherwise pass through!
    '''
    is_a = (len(rgba) == 4)
    if is_a:
        return rgba
    else:
        r, g, b = rgba
        return r, g, b, alpha


def get_colour_type(colour: Union[tuple, str]) -> type:
    '''Check whether colour format is 8-bit, hexidecimal or unit [0.0 -> 1.0]
    '''
    if type(colour) == str:
        return str
    elif any([type(c) == float or type(c) == np.float64 for c in colour]):
        if any([c > 1 for c in colour]):
            raise ValueError('float colours must be between 0 and 1, '
                             + f'got {colour}')
        return float
    else:
        if max(colour) == 1:
            warnings.warn('\n\nMax colour channel is 1 -> this has been '
                          + 'interpreted as an 8bit colour.\n'
                          + 'Please amend to 1.0 for float interpretation.\n')
        return int


def rgb_8bit_to_unit(rgb: tuple) -> tuple:
    '''Convert 8bit rgb to unit [0.0 -> 1.0]
    '''
    def f(x): return x / 255
    return tuple([f(c) for c in rgb])


def rgb_unit_to_8bit(rgb: tuple) -> tuple:
    '''Convert unit [0.0 -> 1.0] to 8bit rgb
    '''
    def f(x): return int(x * 255)
    return tuple([f(c) for c in rgb])


def hex_to_rgba(hex_colour: str) -> tuple:
    '''Convert hexidecimal colour to unit [0.0 -> 1.0]
    '''
    if type(hex_colour) != str:
        raise TypeError('Hex colour expected as string')
    hex_colour = hex_colour.strip('#')
    if len(hex_colour) != 6 and len(hex_colour) != 8:
        raise ValueError('Hex colour expected with string length 6 or 8, '
                         + f'but got {len(hex_colour)}: {hex_colour}')
    length = len(hex_colour)
    hex_list = [hex_colour[i: i + 2] for i in range(0, length, 2)]
    rgba = tuple([int(h, 16) for h in hex_list])
    return rgb_8bit_to_unit(rgba)


if __name__ == "__main__":
    hexi = '#2F009F'
    unit = (0, 0.4, 1.0)
    _8bit = (1, 0, 255, 8)
    print(colour(hexi))
