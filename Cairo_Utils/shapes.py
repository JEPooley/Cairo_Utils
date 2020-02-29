import cairo
import math


class Shapes:

    @classmethod    
    def draw_rectangle(cls, cr, width, height, r, g, b, a=1):
        cr.set_source_rgba(r, g, b, a)
        cr.rectangle(0, 0, width, height)
        cr.fill()

    @classmethod
    def draw_circle_fill(cls, cr, x, y, radius, r, g, b, a=1):
        cr.set_source_rgba(r, g, b, a)
        cr.arc(x, y, radius, 0, 2 * math.pi)
        cr.fill()

    @classmethod
    def draw_circle_fill_shade(cls, cr, x, y, radius, shift, r, g, b, a=1):
        cls.draw_circle_fill(cr, x, y, radius, r, g, b)
        cls.draw_circle_fill(cr, x - shift, y - shift, radius, 0, 0, 0, a=0.1)