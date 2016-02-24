import math
from sampler_base import SamplerBase
from color import Color
from PIL import Image


def clamp(a, minval, maxval):
    return max(minval, min(maxval, a))


def smoothstep(a, b, t):
    t = clamp((t - a) / (b - a), 0.0, 1.0)
    return t * t * t * (t * (t * 6 - 15) + 10)


def length(x, y):
    return math.sqrt(x * x + y * y)


class ImageBlock:
    """
    Represents a rectangular subset of pixels within an image.
    Used to specify which pixels a particular task should be generating.
    """
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def next_pixel(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                yield (self.pos[0] + x, self.pos[1] + y)


class ImageInfo:
    def __init__(self, image):
        """
        Prepares the ImageInfo for use by the application.
        pixelPosition = Integer coordinates within the image
        pos = Coordinates within the image in the 0...1 range
        """
        self.image = image
        self.block = None
        self.pixel = (0, 0)
        self.pos = (0, 0)
        self.pixel_scale = (1.0, 1.0)


class SourceImage:
    def __init__(self, width, height):
        """
        size - A 2-tuple containing (width,height) in pixels.
        """
        self.size = (width, height)
        self.image = Image.new("RGB", self.size, "black")

    def show(self):
        self.image.show()

    def save(self, path):
        self.image.save(path)

    def set_pixel(self, pos, color):
        self.image.putpixel(pos, (int(color.red * 255), int(color.green * 255), int(color.blue * 255)))

    def generate_blocks(self, block_size):
        """
        Generates a list of ImageBlock objects that may be used to generate the entire image.
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
        d = smoothstep(r, r + 0.1, length(x, y))
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
        t = info.pos[0] * math.pi * 2.0
        v = 0.5 + math.sin(t * 8.0 + info.pos[1] * 12.4) * 0.5
        return Color(red=v, green=v, blue=v)

    def checker(self, info):
        """
        This method is used to compute the color of the current pixel.
        Generates a checkerboard pattern.
        :param info: Description of the current sample being computed.
        :return: The computed color value for the pixel being evaluated.
        """
        if info.pos[0] < 0.5:
            if info.pos[1] >= 0.5:
                return self.colorB
        else:
            if info.pos[1] < 0.5:
                return self.colorB
        return self.colorA

    def execute(self, image):
        """
        Generates the pixels for the image block associated with this task.
        :param image: The image which is to contain our generated data.
        :return:
        """
        info = ImageInfo(image)
        # info.pixel_scale = (1.0 / image.size[0], 1.0 / image.size[1])
        info.pixel_scale = (1.0, 1.0)

        # TODO: The sampler will be specified in the definition file
        sampler = SamplerBase(1, 1, info.pixel_scale)

        for pixel in self.block.next_pixel():
            info.pixel = pixel
            clr = Color()
            for sample in sampler.next_sample(pixel[0], pixel[1]):
                info.pos = (sample[0]/image.size[0], sample[1]/image.size[1])
                # clr += self.method(info)
                # clr += self.checker(info)
                clr += self.circle(info)
            image.set_pixel(pixel, clr / len(sampler))


if __name__ == "__main__":
    image = SourceImage((256, 256))

    image_tasks = [ImageTask(x) for x in image.generate_blocks(32)]

    print("Number of tasks = " + str(len(image_tasks)))

    for task in image_tasks:
        task.execute(image)

    image.show()
