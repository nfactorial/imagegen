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

from .output_node import OutputNode
from .node_registry import create_node


def generate_nodes(json_data):
    """
    Generates a Node instance for each definition within the supplied json data.
    :param json_data: The json data containing the description for each node to be created.
    :return: Yields one node instance for each entry within the supplied json data.
    """
    if 'nodes' in json_data:
        for desc in json_data['nodes']:
            node = create_node(desc['name'], desc['type'])
            node.read_json(desc)
            yield node


def generate_output(json_data, nodes):
    """
    Generates an output node for each definition within the supplied json data.
    :param json_data: The json data containing the description for each output node to be created.
    :param nodes: List of nodes the output may be attached to.
    :return: Yields one output node for each entry within the supplied json data.
    """
    if 'output' in json_data:
        for desc in json_data['output']:
            output = OutputNode(desc['name'])
            output.read_json(desc, nodes)
            yield output


def resolve_parameters(node, nodes):
    """
    Given a single node, this method resolves any references to other nodes
    within the parameter list.
    :param node: The node whose parameters are to be resolved.
    :param nodes: List of available nodes for binding.
    """
    for _, param in node.params.items():
        if param.binding is not None:
            param.binding = nodes[param.binding]


def resolve_nodes(nodes):
    """
    Given a list of nodes, this method resolves all the parameters that make
    reference to other nodes.
    :param nodes: List of nodes whose parameters are to be resolved.
    """
    for item in nodes.items():
        resolve_parameters(item[1], nodes)


def create_nodes(json_data):
    """
    Creates a dictionary of nodes from the supplied json data.
    :param json_data: The json data that describes each node to be created.
    :return: List of nodes that were described within the supplied json data.
    """
    nodes = {node.name: node for node in generate_nodes(json_data)}
    resolve_nodes(nodes)
    return nodes


def create_output(json_data, nodes):
    """
    Creates a dictionary of output nodes from the supplied json data.
    :param json_data: The json data that describes the output nodes to be created.
    :param nodes: List of nodes that the output may be attached to.
    :return: List of output nodes that were described within the supplied json data.
    """
    return {output.name: output for output in generate_output(json_data, nodes)}
