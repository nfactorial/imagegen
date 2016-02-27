from node_registry import create_node


def generate_nodes(json_data):
    """
    Generates a Node instance for each definition within the supplied json data.
    :param json_data: The json data containing the description for each node to be created.
    :return: Yields one node instance for each entry within the supplied json data.
    """
    if json_data['nodes'] is not None:
        for x in json_data['nodes']:
            node = create_node(x['name'], x['type'])
            # TODO: Copy over properties for the node
            yield node


def resolve_parameters(node, nodes):
    """
    Given a single node, this method resolves any references to other nodes within the parameter list.
    :param node: The node whose parameters are to be resolved.
    :param nodes: List of available nodes for binding.
    :return:
    """
    for p in node.parameters:
        if p.binding is not None:
            p.binding = nodes[p.binding]


def resolve_nodes(nodes):
    """
    Given a list of nodes, this method resolves all the parameters that make reference to other nodes.
    :param nodes: List of nodes whose parameters are to be resolved.
    :return:
    """
    for node in nodes:
        resolve_parameters(node, nodes)


def create_nodes(json_data):
    """
    Creates a dictionary of nodes from the supplied json data.
    :param json_data: The json data that describes each node to be created.
    :return: List of nodes that were described within the supplied json data.
    """
    nodes = {node.name: node for node in generate_nodes(json_data)}
    resolve_nodes(nodes)
    return nodes
