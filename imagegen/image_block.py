
class ImageBlock:
    """
    Represents a rectangular subset of pixels within an image.
    Used to specify which pixels a particular task should be generating.
    """
    def __init__(self, pos, size):
        """
        :param pos: The pixel position within the image where the top left of the image block begins.
        :param size: Tuple containing the width and height (in pixels) of the image block.
        """
        self.pos = pos
        self.size = size

    @property
    def x(self):
        """
        Gets the position along the horizontal axis of the image block object.
        :return: The position along the horizontal axis of the image block.
        """
        return self.pos[0]

    @property
    def y(self):
        """
        Gets the position along the vertical axis of the image block object.
        :return: The position along the vertical axis of the image block.
        """
        return self.pos[1]

    @property
    def width(self):
        """
        Gets the width (in pixels) of the image block object.
        :return: The width (in pixels) of the image block.
        """
        return self.size[0]

    @property
    def height(self):
        """
        Gets the height (in pixels) of the image block object.
        :return: The height (in pixels) of the image block object.
        """
        return self.size[1]

    def next_pixel(self):
        """
        Generator function that returns the coordinates of each pixel within the ImageBlock object.
        :return: The next pixel within the image block that should be processed.
        """
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                yield (self.pos[0] + x, self.pos[1] + y)
