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

from collections import namedtuple

from .node import Node

# This tuple describes a registered node within the application.
NodeDefinition = namedtuple('NodeDefinition', ['name',
                                               'evaluate',
                                               'input',
                                               'output',
                                               'description'])


# This dictionary contains all the nodes currently registered
NODE_REGISTRY = {}


class NodeExistsError(Exception):
    """
    This exception is raised by imagegen when a node is registered that already exists.
    """
    def __init__(self, name):
        """
        Prepares the exception for use by the application.
        :param name: Name of the node that caused the exception to be raised.
        """
        super(NodeExistsError, self).__init__(name)
        self.name = name

    def __str__(self):
        """
        Creates a string representation of the exception.
        :return: The string representation of the exception.
        """
        return 'The node \'' + self.name + '\' already exists within the registry.'


def register_node(name, eval_func, input_args, output=None, description=None):
    """
    Attempts to register a new node with the node registry.
    :param name: Name of the node being registered.
    :param eval_func: The function to be invoked when the node contents should be evaluated.
    :param input_args: The parameters the node requires to compute its result.
    :param output: The parameter the node will compute.
    :param description: Descriptive text for the node.
    """
    if name in NODE_REGISTRY:
        raise NodeExistsError(name)

    NODE_REGISTRY[name] = NodeDefinition(name, eval_func, input_args, output, description)


def unregister_node(name):
    """
    Removes a registered node from the applications registry.
    :param name: Name of the node type to be removed.
    """
    if name in NODE_REGISTRY:
        del NODE_REGISTRY[name]


def create_node(name, node_type):
    """
    Create an instance of a node associated with the specified name.
    :param name: The name to be associated with the newly created node.
    :param node_type: The type of node to be instantiated.
    :return: The newly created node of the specified type.
    """
    if node_type in NODE_REGISTRY:
        return Node(name, NODE_REGISTRY[node_type])
    raise TypeError('The specified node type \'' + node_type +
                    '\' could not be found within imagegen.')
