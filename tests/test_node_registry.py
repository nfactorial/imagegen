# test_node_registry.py

import unittest

from imagegen.color import Color
from imagegen.node_registry import register_node
from imagegen.parameter import ParameterDefinition

test_input = [
    ParameterDefinition('background', param_type='color', default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('color', param_type='color', default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0)),
]


class TestNodeRegistry(unittest.TestCase):
    def test_register(self):
        register_node('TestNode', test_input, output='color')
        self.failureException(register_node('TestNode', test_input, output='color'))
