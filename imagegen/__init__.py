"""
Run unit tests with....
python -m unittest discover tests
"""

from source_image import SourceImage, ImageTask

job_size = 32

# image = SourceImage(256, 256)
image = SourceImage(256, 256)
image_tasks = [ImageTask(x) for x in image.generate_blocks(job_size)]

print("Number of tasks = " + str(len(image_tasks)))

for task in image_tasks:
    task.execute(image)

image.show()
image.save('output.png')
