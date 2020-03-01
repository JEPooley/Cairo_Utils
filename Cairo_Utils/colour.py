
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