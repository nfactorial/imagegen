
class SamplerBase:
    """
    Base class for all samplers available for use within the application.
    A sampler generates one or more samples for a single pixel, the layout of the generated
    samples is defined by the type of sampler being used.
    The basic sampler generates one sample in the center of the specified pixel.
    """
    def __init__(self, x_samples, y_samples, pixel_scale):
        """
        Prepares the sampler for use by the application.
        :param x_samples: The number of samples to be generated along the horizontal axis.
        :param y_samples: The number of samples to be generated along the vertical axis.
        """
        self.x_samples = x_samples
        self.y_samples = y_samples
        self.pixel_scale = pixel_scale
        self.dx = 1.0 / x_samples
        self.dy = 1.0 / y_samples

    def __len__(self):
        return 1

    def next_sample(self, x, y):
        """
        Generates a list of samples for the given pixel.
        :param x: Position of the pixel along the horizontal axis.
        :param y: Position of the pixel along the vertical axis.
        :return: Tuple containing the x,y floating point coordinates of the sample.
        """
        # We add 0.5 to the pixel position, as we treat 0.5 as the pixels center
        yield x + (0.5 * self.pixel_scale[0]), y + (0.5 * self.pixel_scale[1])
