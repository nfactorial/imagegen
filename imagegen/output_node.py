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

from multiprocessing import Pool

from .output_image import OutputImage
from .image_block import execute_block


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

    @property
    def filename(self):
        """
        Returns the filename for the image generated by this node.
        TODO: This function will be made more robust in the future
        :return: The filename the image is expected to be stored under.
        """
        return self.name + '.' + self.file_type

    def generate_image(self, job_size=32):
        """
        This method generates an image for this output node. If the output node is not connected then no image
        will be generated.
        :param job_size: The size of the worker job, default is 32.
        :return: The OutputImage object generated by this node.
        """
        if self.node is not None:
            image = OutputImage(self.width, self.height)
            for block in image.generate_blocks(job_size):
                # TODO: Hand off to a scheduler
                block.execute(self)
            return image

    def generate_image_async(self, job_size=32):
        """
        Research function to use simple multiprocessing on our task list.
        Unfortunately doesn't currently work, due to the cross-process memory access.
        Left here for future reference, though I'll probably resort to GPU processing instead.
        :param job_size: The size of the worker job, default is 32.
        :return: The OutputImage object generated by this node.
        """
        pool = Pool(processes=4)
        image = OutputImage(self.width, self.height)
        results = [pool.apply_async(execute_block, (block, self)) for block in image.generate_blocks(job_size)]
        print([res.get() for res in results])
