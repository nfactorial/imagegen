
class SamplerBase:
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

    def dump(self):
        print('x_samples = ' + str(self.x_samples))
        print('y_samples = ' + str(self.y_samples))
        print('pixel_scale[0] = ' + str(self.pixel_scale[0]))
        print('pixel_scale[1] = ' + str(self.pixel_scale[1]))
        print('samples = ' + str(len(self)))

    def __len__(self):
        return 1

    def next_sample(self, x, y):
        # We add 0.5 to the pixel position, as we treat 0.5 as the pixels center
        yield x + (0.5 * self.pixel_scale[0]), y + (0.5 * self.pixel_scale[1])
