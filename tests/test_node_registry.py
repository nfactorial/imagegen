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

import unittest

from imagegen.node import Node
from imagegen.color import Color
from imagegen.node_registry import register_node, unregister_node, create_node, NodeExistsError
from imagegen.parameter import ParameterDefinition

TEST_INPUT = [
    ParameterDefinition('background',
                        param_type='color',
                        default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('color',
                        param_type='color',
                        default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0)),
]

INVALID_NODE_TYPE = 'unittest.invalid.node.type'
TEST_NODE_OUTPUT = 'Color'
TEST_NODE_TYPE = 'TestNode'
TEST_NODE_NAME = 'Testing'


def evaluate_test(eval_info):
    return Color()


class TestRegistration(unittest.TestCase):
    """
    This test ensures the node registry correctly handles the addition
    and removal of nodes.
    This is a separate test so that we can verify this behaviour before
    moving onto the unit tests that make use of these functions.
    """
    def test_register(self):
        register_node(TEST_NODE_TYPE, evaluate_test, TEST_INPUT, output=TEST_NODE_OUTPUT)
        self.assertRaises(NodeExistsError,
                          register_node, TEST_NODE_TYPE, evaluate_test, TEST_INPUT,
                          output=TEST_NODE_OUTPUT)
        unregister_node(TEST_NODE_TYPE)
        register_node(TEST_NODE_TYPE, evaluate_test, TEST_INPUT, output=TEST_NODE_OUTPUT)
        unregister_node(TEST_NODE_TYPE)


class TestNodeRegistry(unittest.TestCase):
    def setUp(self):
        register_node(TEST_NODE_TYPE, evaluate_test, TEST_INPUT, output=TEST_NODE_OUTPUT)

    def tearDown(self):
        unregister_node(TEST_NODE_TYPE)

    def test_missing(self):
        """
        Check an exception is correctly thrown when we attempt to create
        a node type that doesn't exist.
        """
        self.assertRaises(TypeError, create_node, TEST_NODE_NAME, INVALID_NODE_TYPE)

    def test_creation(self):
        """
        Check we can successfully create a node that has been registered.
        """
        node = create_node(TEST_NODE_NAME, TEST_NODE_TYPE)
        self.assertIsNotNone(node)
        self.assertTrue(isinstance(node, Node))
        self.assertEqual(node.name, TEST_NODE_NAME)
        self.assertEqual(len(node.params), len(TEST_INPUT))
        self.assertEqual(node.evaluate, evaluate_test)
