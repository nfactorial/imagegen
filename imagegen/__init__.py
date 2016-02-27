"""
Run unit tests with....
python -m unittest discover tests
"""

import sys
import imagegen.nodes

from source_image import SourceImage, ImageTask

print('len(argv) = ' + str(len(sys.argv)))
for x in sys.argv:
    print(x)


job_size = 32

image = SourceImage(256, 256)
image_tasks = [ImageTask(x) for x in image.generate_blocks(job_size)]

print("Number of tasks = " + str(len(image_tasks)))

for task in image_tasks:
    task.execute(image)

image.show()
image.save('output.png')
