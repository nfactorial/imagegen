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

# We split all images that are to be processed into smaller rectangles of 'work'
# This is to allow us to distribute these tasks to separate threads in the future.
image = SourceImage(256, 256)
image_tasks = [ImageTask(x) for x in image.generate_blocks(job_size)]

print("Number of tasks = " + str(len(image_tasks)))

for task in image_tasks:
    task.execute(image)

image.show()
image.save('output.png')
