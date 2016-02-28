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


class OutputNode:
    """
    This class describes an image that may be output from the application.
    """
    def __init__(self, name):
        self.name = name
        self.file_type = 'png'
        self.width = 256
        self.height = 256
        self.format = 'RGB'
        self.sampler = None
        self.node = None

    def read_json(self, desc, nodes):
        """
        Reads the content of the supplied json data.
        :param desc: The json formatted description of the output node.
        :param nodes: Dictionary of nodes we may be attached to.
        """
        if 'type' in desc:
            self.file_type = desc['type']
        if 'width' in desc:
            self.width = desc['width']
        if 'height' in desc:
            self.height = desc['height']
        if 'format' in desc:
            self.format = desc['format']
        # TODO: Need to read 'sampler' also
        if 'node' in desc:
            if desc['node'] not in nodes:
                raise TypeError('Could not resolve node reference \'' + desc['node'] + '\' in output node \'' + self.name + '\'.')
            self.node = nodes[desc['node']]
