import random


class Colour:

    @classmethod
    def unpack_rgba(cls, rgba: tuple):
        is_a = (len(rgba) == 4)
        if is_a:
            r, g, b, a = rgba
            return r, g, b, a
        else:
            r, g, b = rgba
            return r, g, b, 1

    @classmethod
    def rgb_8bit_to_unit(cls, rgb):
        def f(x): return x/255
        return tuple([f(c) for c in rgb])

    @classmethod
    def rgb_unit_to_8bit(cls, rgb):
        def f(x): return int(x * 255)
        return tuple([f(c) for c in rgb])

    @classmethod
    def random_colour(cls, unit_interval=False):
        def r(): return random.randint(0, 255)
        rgb_8bit = (r(), r(), r())
        if unit_interval:
            return cls.rgb_8bit_to_unit(rgb_8bit)
        return rgb_8bit

    @classmethod
    def add_alpha(cls, rgb, alpha):
        channels = len(rgb)
        assert channels == 3, f'rgb should be 3-channel, got {channels}\n'\
            + f'>>> {rgb}'
        return rgb + (alpha,)


if __name__ == "__main__":
    rgb = Colour.random_colour() + (5,)
    print(Colour.add_alpha(rgb, 0.1))
