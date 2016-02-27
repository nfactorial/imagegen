# External imports
import math
from PIL import Image

# Internal imports
from color import Color
from math_help import smooth_step, length
from image_block import ImageBlock
from sampler_base import SamplerBase


class ImageInfo:
    def __init__(self, image):
        """
        Prepares the ImageInfo for use by the application.
        pixelPosition = Integer coordinates within the image
        pos = Coordinates within the image in the 0...1 range
        """
        self.image = image
        self.block = None
        self.rotation = 0
        self.pixel = (0, 0)
        self.pos = (0, 0)
        self.sample = (0, 0)
        self.pixel_scale = (1.0, 1.0)


class SourceImage:
    def __init__(self, width, height):
        """
        Prepares the source image for use by the application.
        :param width: The width of the image (in pixels)
        :param height: The height of the image (in pixels)
        """
        self.size = (width, height)
        self.image = Image.new('RGB', self.size, 'black')

    def show(self):
        self.image.show()

    def save(self, path):
        self.image.save(path)

    def set_pixel(self, pos, color):
        self.image.putpixel(pos, (int(color.red * 255), int(color.green * 255), int(color.blue * 255)))

    def generate_blocks(self, block_size):
        """
        Generates a list of ImageBlock objects that may be used to generate the entire image.
        :param block_size: The size of a single image block (in pixels).
        :return:
        """
        x = 0
        while x < self.size[0]:
            y = 0
            while y < self.size[1]:
                yield ImageBlock((x, y), (min(block_size, self.size[0] - x), min(block_size, self.size[1] - y)))
                y += block_size
            x += block_size


class ImageTask:
    def __init__(self, block):
        """
        Prepares the task for use by the application.
        """
        self.colorA = Color(red=0.0, green=0.0, blue=0.0)
        self.colorB = Color(red=1.0, green=1.0, blue=1.0)
        self.block = block

    def method(self, info):
        """
        This method is used to compute the color of the current pixel.
        Multiple methods will eventually be provided and selected between
        """
        color = (1.0, 0.4, 0.1)
        x = info.pos[0] - 0.5
        y = info.pos[1] - 0.5
        r = 0.2 + 0.1 * math.cos(math.atan2(y, x) * 10.0)
        d = smooth_step(r, r + 0.1, length(x, y))
        return Color(red=color[0] * d, green=color[1] * d, blue=color[2] * d)

    def circle(self, info):
        x = info.pos[0] - 0.5
        y = info.pos[1] - 0.5
        d = math.sqrt(x*x + y*y)
        # a = math.atan2(y, x)
        # if 0.3 < d < 0.35:
        #    if a < 1.0:
        #        return self.colorB
        if 0.3 < d < 0.35:
            return self.colorB
        return self.colorA

    def sine_stripe(self, info):
        v = 0.5 + math.sin(info.pos[0] * 32.0) * 0.5
        return self.colorA.lerp(self.colorB, v)

    def checker(self, info):
        """
        This method is used to compute the color of the current pixel.
        Generates a checkerboard pattern.
        :param info: Description of the current sample being computed.
        :return: The computed color value for the pixel being evaluated.
        """
        x = math.fmod(info.pos[0], 1.0)
        y = math.fmod(info.pos[1], 1.0)
        if x < 0.5:
            if y >= 0.5:
                return self.colorB
        else:
            if y < 0.5:
                return self.colorB
        # if info.pos[0] < 0.5:
        #    if info.pos[1] >= 0.5:
        #        return self.colorB
        # else:
        #    if info.pos[1] < 0.5:
        #        return self.colorB
        return self.colorA

    def complex_checker(self, info):
        """
        Test function that computes a checkerboard pattern, with a contained image.
        :param info:
        :return:
        """
        bx = math.fmod(info.pos[0], 1.0)
        by = math.fmod(info.pos[1], 1.0)
        if bx < 0.5:
            if by >= 0.5:
                return self.colorB
        else:
            bx -= 0.5
            if by < 0.5:
                return self.colorB
            by -= 0.5

        sub_info = ImageInfo(info.image)
        sub_info.pixel = info.pixel

        sampler = SamplerBase(1, 1, (info.pixel_scale[0] * 0.5, info.pixel_scale[1] * 0.5))

        color = Color()
        for sub_info.pos in sampler.next_sample((bx / 0.5, by / 0.5)):
            color += self.circle(sub_info)
        color /= len(sampler)
        return color

    def evaluate_pixel(self, info, sampler):
        """
        Computes the color of a pixel within an image.
        :param info: Description of the pixel being evaluated.
        :param sampler: The sampler to be used when computing the pixel color.
        :return: The color of the specified pixel.
        """
        color = Color()
        for info.pos in sampler.next_sample(info.pixel):
            # color += self.method(info)
            # color += self.checker(info)
            # color += self.complex_checker(info)
            color += self.circle(info)
            # color += self.sine_stripe(info)

        return color / len(sampler)

    def evaluate_block(self, info, block, sampler):
        """
        Generator function that returns the position and color of each pixel within the specified image block.
        :param info: Description of the image being evaluated.
        :param block: Description of the image block being evaluated.
        :param sampler: The sampler to be used when computing the pixel color.
        :return: Tuple containing (pixel coordinates, pixel color).
        """
        for pixel in block.next_pixel():
            info.pixel = (pixel[0] * sampler.pixel_scale[0], pixel[1] * sampler.pixel_scale[1])
            yield pixel, self.evaluate_pixel(info, sampler)

    def execute(self, image):
        """
        Computes the color of an image using the current graph tree.
        :param image: The image whose content is to be calculated.
        :return:
        """
        info = ImageInfo(image)
        info.pixel_scale = (1.0 / image.size[0], 1.0 / image.size[1])

        # TODO: The sampler will be specified in the definition file
        sampler = SamplerBase(1, 1, info.pixel_scale)

        # image.set_pixel(for pixel, color in self.evaluate_block(info, self.block, sampler))
        # [image.set_pixel(pixel, color) for pixel, color in self.evaluate_block(info, self.block, sampler)]
        # image.set_pixel(pixel, color for pixel, color in self.evaluate_block(info, self.block, sampler))
        # image.set_pixel(pixel, color) (for pixel, color in self.evaluate_block(info, self.block, sampler))
        for pixel, color in self.evaluate_block(info, self.block, sampler):
            image.set_pixel(pixel, color)
