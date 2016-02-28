"""
Run unit tests with....
python -m unittest discover tests
"""

import sys
import json

from .nodes import *

from loader import create_nodes
from source_image import SourceImage, ImageTask

"""
print('len(argv) = ' + str(len(sys.argv)))
for x in sys.argv:
    print(x)


nodes = None

with open('examples/checker.json') as f:
    data = json.load(f)
    nodes = create_nodes(data)

print('Node hierarchy created, number of nodes = ' + str(len(nodes)))
for key, n in nodes.items():
    print('Node - type = ' + n.definition.name + ', name = ' + n.name)
"""

job_size = 32

# We split all images that are to be processed into smaller rectangles of 'work'
# This is to allow us to distribute these tasks to separate threads in the future.
image = SourceImage(256, 256)
image_tasks = [ImageTask(x) for x in image.generate_blocks(job_size)]

print("Number of tasks = " + str(len(image_tasks)))

for task in image_tasks:
    task.execute(image)

image.show()
image.save('output.png')
