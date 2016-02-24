import json
from node import Node


class Loader:
    """
    This class implements the logic that loads an image generation file from the hard-drive and prepares
    imagegen for processing.
    """
    def __init__(self, path):
        self.nodes = None
        self.path = path
        with open(path, 'r') as f:
            self.load_nodes(json.load(f))

    # Once everything has been loaded, the application then calls 'generateTasks'. This will walk the
    # graph defined within the generation tree and spit out the tasks necessary for producing the image.
    # the list of tasks is then passed onto the scheduler for processing.
    # Once complete, we are left with all nodes containing their generated images (if necessary) and we
    # can produce the final image.

    def load_nodes(self, json_data):
        if json_data[ 'nodes' ] is not None:
            self.nodes = [Node(x) for x in json_data['nodes']]
