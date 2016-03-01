IMAGEGEN
========
This python module provides some simple functionality for generating procedural images using Python code.

Images are formed by connecting various nodes within a graph, the module then processes the graph to produce
the output image. Image graphs are defined within a JSON formatted file.

The main goal of the project is mostly to practice Python with a relatively fun project.

## Build status

| [Linux][lin-link] |
| :---------------: |
| ![lin-badge]      |

[lin-badge]: https://travis-ci.org/nfactorial/imagegen.svg?branch=master "Travis build status"
[lin-link]:  https://travis-ci.org/nfactorial/imagegen "Travis build status"

USAGE
=====
Imagegen currently require PIL or Pillow to be installed (https://pillow.readthedocs.org/en/3.0.0/installation.html).
If you have pip installed, Pillow can be added easily with:

```
pip install Pillow
```

Imagegen requires an image definition file to be supplied, this file is a JSON formatted document that describes
the image you wish to be generated. Some simple examples are included inside the examples folder. Once you have
an image definition file, you may run imagegen from the command line:

```
python -m imagegen -f {filename}
```

Where you must specify the filename of your definition file in place of the {filename}. Imagegen will then load
the json data and produce the output images.

To obtain a list of the nodes available in the current version of imagegen, we can ask it to list them from the
command line:

```
python -m imagegen --nodes
```

Nodes will be described later in this document.

PERFORMANCE
===========
Imagegen currently performs all evaluation on the CPU and thus performance is restricted to the speed of the host
processor. This means imagegen is really only suitable for offline processing, however once the framework has
stabilised I will be looking into moving as much processing to the GPU where possible. The intent being to have
most or all processing on the GPU with the CPU as a fallback.

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

![Checkerboard Example](/images/checkerboard_a.png)

The checkerboard node contains two properties that specify each color used by the pattern. However, we can alter
one of the color properties to reference the circle image we used in the previous examples. Regenerating the image
results in the following output:

![Checkerboard with circle example](/images/checker_circle.png)

We can also adjust the scaling of the checkerboard pattern, which creates a more complicated image for very little
work:

![Checkerboard with circle and scale example](/images/checker_circle2.png)

And we can adjust the rotation of the checkerboard node by setting its rotation property:

![Checkerboard with circle, scale and rotation example](/images/checker_circle3.png)

OUTPUT
======
Imagegen is capable of outputting multiple images from a single graph, the image results are defined by the
output node. This allows imagegen to compute various attributes of a particular image, such as diffuse,
specular and normal maps. Making it suitable for offline generation of textures for use within a 3D application.

NOISE
=====
An important part of procedural image generation is the noise primitive. Imagegen provides support for noise
generation using the noise library (https://pypi.python.org/pypi/noise/). However, I'm still in the process of
determining how the nodes are to be exposed (as well as which noise functions). Please be aware that the
definition of the noise nodes may change in the short term future. Once they have become more concrete this
documentation will be updated. An example noise image generated using imagegen can be seen below, this image
was generated using the JSON definition found inside the examples folder (examples/noise_test.json).

![Noise Example](/images/noise_a.png)

