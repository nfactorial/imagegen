"""
Copyright 2016 nfactorial

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .math_help import rotate_origin


class EvalInfo:
    """
    Contains the properties necessary for a node to evaluate its result for a particular sample.
    The intent of the EvalInfo object is to supply an evaluation function with the data necessary
    for computing its resulting value, abstracting away the complexity of how the parameters are
    actually computed.
    The EvalInfo object contains the x,y coordinates of the sample being evaluated.
    """
    def __init__(self, node):
        if node is None:
            raise TypeError
        self.node = node
        self.image_size = (0,0)
        self.pixel_size = (0.0, 0.0)
        self.x = 0.0
        self.y = 0.0

    @property
    def pos(self):
        """
        Returns Tuple containing x, y position being evaluated.
        :return: Tuple x, y position being evaluated.
        """
        return self.x, self.y

    def evaluate(self, name, x, y):
        """
        Evaluates the value of a parameter at the specified sample position.
        :param name: String containing the name of the parameter to be evaluated.
        :param x: Position of the sample to be evaluated along the horizontal axis.
        :param y: Position of the sample to be evaluated along the vertical axis.
        :return: The computed result of the parameter.
        """
        p = self.node.params[name]
        if p.binding:
            p.binding.generate_image()
            info = EvalInfo(p.binding)
            info.image_size = self.image_size
            info.pixel_size = self.pixel_size
            info.x, info.y = rotate_origin((x * p.binding.scaling[0], y * p.binding.scaling[1]),
                                           (0.5, 0.5),
                                           p.binding.rotation)
            return p.binding.evaluate(info)
        return p.current_value
