
class StratifiedSampler:
    def __init__(self, x_samples, y_samples):
        self.x_samples = x_samples
        self.y_samples = y_samples
        self.dx = 1.0 / x_samples
        self.dy = 1.0 / y_samples

    def get_samples(self, x, y):
        for x_loop in range(self.x_samples):
            for y_loop in range(self.y_samples):
                yield