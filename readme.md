IMAGEGEN
========
This python module provides some simple functionality for generating procedural images using Python code.

Images are formed by connecting various nodes within a graph, the module then processes the graph to produce
the output image. Image graphs are defined within a JSON formatted file.

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

Currently only stratified sampling has been provided, whilst useful it is not the only anti-aliasing method
nor is it the best for all situations. The list of available sampling methods will be increased in the
future.

If we enable stratified sampling and re-generate the aliased image above, imagegen outputs the following
result:

![SuperSampled Circle](/images/ss_circle.png)

As we can see, the curved boundaries on this image look much smoother and more pleasing to the eye. Care should
be taken when enabling stratified sampling, as the feature increases the number of samples evaluated
for each pixel in the iage and thus also increases the length of time taken to generate the output.
