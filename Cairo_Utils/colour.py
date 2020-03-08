import random

from typing import Union


def colour(colour: Union[tuple, str]) -> tuple:
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
    def r(): return random.random()
    if rand_alpha:
        return (r(), r(), r(), r())
    else:
        return (r(), r(), r(), 1)


def unpack_rgba(rgba: tuple, alpha: float = 1.0) -> tuple:
    is_a = (len(rgba) == 4)
    if is_a:
        r, g, b, a = rgba
        return r, g, b, a
    else:
        r, g, b = rgba
        return r, g, b, alpha


def get_colour_type(colour: Union[tuple, str]) -> type:
    if type(colour) == str:
        return str
    elif any([type(c) == float for c in colour]):
        if any([c > 1 for c in colour]):
            raise ValueError('float colours must be between 0 and 1, '
                             + f'got {colour}')
        return float
    else:
        return int


def rgb_8bit_to_unit(rgb: tuple) -> tuple:
    def f(x): return x / 255
    return tuple([f(c) for c in rgb])


def rgb_unit_to_8bit(rgb: tuple) -> tuple:
    def f(x): return int(x * 255)
    return tuple([f(c) for c in rgb])


def hex_to_rgba(hex_colour: str) -> tuple:
    if type(hex_colour) != str:
        raise TypeError('Hex colour expected as string')
    if len(hex_colour) != 7 and len(hex_colour) != 9:
        raise ValueError('Hex colour expected with string length 7 or 9, '
                         + f'but got {len(hex_colour)}: {hex_colour}')
    hex_colour = hex_colour.strip('#')
    length = len(hex_colour)
    hex_list = [hex_colour[i: i + 2] for i in range(0, length, 2)]
    rgba = tuple([int(h, 16) for h in hex_list])
    return rgb_8bit_to_unit(rgba)


if __name__ == "__main__":
    hexi = '#2F009F0A'
    unit = (0, 0.4, 1.0)
    _8bit = (1, 0, 255, 8)
    print(colour(hexi))
