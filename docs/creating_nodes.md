Creating Nodes
==============
Imagegen evaluates its output image using a tree graph of interconnected nodes. A node is the main computation
point for each evaluation step of an image. Many nodes are provided by default for use when constructing an
image to be generated, however it is also possible to extend imagegen further with your own custom nodes.

evaluate
--------
The evaluate method is where a nodes work is performed, whenever imagegen would like a sample computed on a
node, it will invoke the evaluate method on it. The evaluate method is supplied an object which describes the
current sample being computed and the node should take this supplied information in order to produce a color
appropriate for the sample.

This document covers the creation of a custom node suitable for use within imagegen.

NodeBase
--------
All node objects must inherit from NodeBase