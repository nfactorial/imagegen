import random
from sampler_base import SamplerBase


class StratifiedSampler(SamplerBase):
    """
    Implements a Sampler object that generates a number of random samples within an area of interest.
    """
    def __len__(self):
        """
        Calculates the number of samples that will be generated by this sampler.
        :return: The number of samples generated by this sampler.
        """
        return self.x_samples * self.y_samples

    def next_sample(self, x, y):
        for x_loop in range(self.x_samples):
            for y_loop in range(self.y_samples):
                x_jitter = random.random()
                y_jitter = random.random()
                # yield x + (0.5 * self.pixel_scale[0]), y + (0.5 * self.pixel_scale[1])
                yield x + (x_jitter * self.pixel_scale[0]), y + (y_jitter * self.pixel_scale[1])