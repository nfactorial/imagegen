IMAGEGEN
========
This python module provides some simple functionality for generating procedural images using Python code.

Images are formed by connecting various nodes within a graph, the module then processes the graph to produce
the output image. Image graphs are defined within a JSON formatted file.

The main goal of the project is mostly to practice Python with a relatively fun project.

EXAMPLES
========
The examples folder contains a selection of simple image graphs that may be executed to produce some example
images.

SAMPLING
========
By default, imagegen performs a single sample per-pixel in the node being evaluated. For many operations this
is sufficient and the resulting image can be used as is. However if the generated image contains quickly
changing data the resulting image can appear 'aliased' with clearly missing data. As an example, take this
generated image of a circle that was created using imagegen:

![Aliased Circle](/images/aliased_circle.png)

As can be seen in this image, the curved boundaries of the circle do not appear smooth to the eye, this
is caused by the sampling of each pixel missing data in-between the samples. To combat these artifacts
imagegen supports super-sampling options on each node.

Currently only stochastic sampling has been provided, whilst useful it is not the only anti-aliasing method
nor is it the best for all situations. The list of available sampling methods will be increased in the
future.

If we enable stochastic sampling and re-generate the aliased image above, imagegen outputs the following
result:

![SuperSampled Circle](/images/ss_circle.png)

As we can see, the curved boundaries on this image look much smoother and more pleasing to the eye. Care should
be taken when enabling stochastic sampling, as the feature increases the number of samples evaluated
for each pixel in the image and thus also increases the length of time taken to generate the result.

NODES
=====
Because imagegen uses a node graph to compute the resulting image, we can combine multiple nodes together to
form more complex images. This allows an image to be broken into its sub-parts and allows the author to develop
each part individually.

As an example, the following image was generated using the default checkerboard node provided within imagegen:

[Checkerboard Example](/images/checkerboard_a.png)

The checkerboard node contains two properties that specify each color used by the pattern. However, we can alter
one of the color properties to reference the circle image we used in the previous examples. Regenerating the image
results in the following output:

[Checkerboard with circle example](/images/checker_circle.png)

OUTPUT
======
Imagegen is capable of outputting multiple images from a single graph, the image results are defined by the
output node. This allows a imagegen to compute various attributes of a particular image, such as diffuse,
specular and normal maps. Making it suitable for offline generation of textures for use within a 3D application.

PERFORMANCE
===========
Imagegen currently performs all evaluation on the CPU and thus performance is restricted to the speed of the host
processor. This means imagegen is really only suitable for offline processing, however once the framework has
stabilised I will be looking into moving as much processing to the GPU where possible.
