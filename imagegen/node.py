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

from .parameter import Parameter


class Node:
    """
    The node class is used to represent a single step within the generated output.
    Nodes may be tied together within the generation graph to allow for more
    complex image generation.
    """
    def __init__(self, name, definition):
        """
        Prepares the node for use by the application.
        :param definition: The NodeDefinition (see node_registry.py) named tuple
                           which describes the node we're representing.
        """
        self.name = name
        self.rotation = 0.0
        self.origin = (0.5, 0.5)
        self.scaling = (1.0, 1.0)
        self.definition = definition
        self.params = {p.name: Parameter(p) for p in definition.input}

    @property
    def evaluate(self):
        """
        :return: The evaluation function associated with this node.
        """
        return self.definition.evaluate

    @property
    def output(self):
        """
        :return: String containing the output type that is return by the nodes evaluation.
        """
        return self.definition.output

    def read_json(self, desc):
        """
        Reads all properties for the node that have been defined within the supplied JSON data.
        :param desc: JSON data describing the nodes properties.
        """
        if 'origin' in desc:
            self.origin = (desc['origin'][0], desc['origin'][1])
        else:
            self.origin = (0.0, 0.0)
        if 'rotation' in desc:
            self.rotation = desc['rotation']
        else:
            self.rotation = 0.0
        if 'scaling' in desc:
            self.scaling = (desc['scaling'][0], desc['scaling'][1])
        else:
            self.scaling = (1.0, 1.0)
        if 'params' in desc:
            for p in desc['params']:
                if p['name'] in self.params:
                    self.params[p['name']].read_json(p)
                else:
                    print('Warn: Parameter \'%s\' does not exist in node type \'%s\'.' %
                          (p['name'], self.definition.name))
