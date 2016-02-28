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

"""
Run unit tests with....
python -m unittest discover tests
"""

import json
import os.path
import argparse

from .nodes import *

from project import Project
from source_image import SourceImage, ImageTask

parser = argparse.ArgumentParser(description='Imaggen - by nfactorial', prog='imagegen')
parser.add_argument('-f', dest='filename', required=True,
                    help='The filename of the JSON definition file containing the image to be generated.')
args = parser.parse_args()

if not os.path.exists(args.filename):
    print('Imagegen - ERROR - Could not locate file \'' + args.filename + '\'.')
    exit()

project = Project()
project.load_json(args.filename)

print('Node hierarchy created, number of nodes = ' + str(len(project.nodes)))
print('Number of output nodes = ' + str(len(project.output)))
for key, n in project.nodes.items():
    print('Node - type = ' + n.definition.name + ', name = ' + n.name)
for key, o in project.output.items():
    print('Output - name = ' + o.name)

job_size = 32

for _, output in project.output.items():
    if output.node is not None:
        image = SourceImage(output.width, output.height)
        # We split all images that are to be processed into smaller rectangles of 'work'
        # This is to allow us to distribute these tasks to separate threads in the future.
        image_tasks = [ImageTask(x) for x in image.generate_blocks(job_size)]
        for task in image_tasks:
            task.execute2(image, output)
        image.save(output.name + '.' + output.file_type)
        image.show()

"""
image = SourceImage(256, 256)
image_tasks = [ImageTask(x) for x in image.generate_blocks(job_size)]

print("Number of tasks = " + str(len(image_tasks)))

for task in image_tasks:
    task.execute(image)

image.show()
image.save('output.png')
"""
