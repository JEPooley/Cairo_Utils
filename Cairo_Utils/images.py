import cairo as cr


class Images:
    '''Manipulate images and add them to an image surface
    '''

    def __init__(self, ctx: cr.Context):
        self._ctx = ctx

    def add_image(self, image_path: str, top: float, left: float,
                  height: float, width: float):
        '''Scale image and add to canvas
        '''
        image_surface = cr.ImageSurface.create_from_png(image_path)
        img_height = image_surface.get_height()
        img_width = image_surface.get_width()
        width_ratio = float(width) / float(img_width)
        height_ratio = float(height) / float(img_height)
        scale_xy = (height_ratio, width_ratio)

        self._ctx.save()
        self._ctx.translate(left, top)
        self._ctx.scale(*scale_xy)
        self._ctx.set_source_surface(image_surface)

        self._ctx.paint()
        self._ctx.restore()
