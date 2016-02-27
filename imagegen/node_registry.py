from imagegen.node import Node
from collections import namedtuple

# This tuple describes a registered node within the application.
NodeDefinition = namedtuple('NodeDefinition', ['evaluate', 'input', 'output'])


# This dictionary contains all the nodes currently registered
imagegen_node_registry = {}


class NodeExistsError(Exception):
    """
    This exception is raised by imagegen when a node is registered that already exists.
    """
    def __init__(self, name):
        """
        Prepares the exception for use by the application.
        :param name: Name of the node that caused the exception to be raised.
        """
        self.name = name

    def __str__(self):
        """
        Creates a string representation of the exception.
        :return: The string representation of the exception.
        """
        return 'The node \'' + self.name + '\' already exists within the registry.'


def register_node(name, eval_func, input_args, output=None):
    """
    Attempts to register a new node with the node registry.
    :param name: Name of the node being registered.
    :param eval_func: The function to be invoked when the node contents should be evaluated.
    :param input_args: The parameters the node requires to compute its result.
    :param output: The parameter the node will compute.
    :return:
    """
    if name in imagegen_node_registry:
        raise NodeExistsError(name)

    imagegen_node_registry[name] = NodeDefinition(eval_func, input_args, output)


def create_node(name, node_type):
    """
    Create an instance of a node associated with the specified name.
    :param name: The name to be associated with the newly created node.
    :param node_type: The type of node to be instantiated.
    :return: The newly created node of the specified type.
    """
    if node_type in imagegen_node_registry:
        return Node(name, imagegen_node_registry[node_type])
    raise NodeExistsError(name)                 # TODO: Should be 'NotFound' exception
