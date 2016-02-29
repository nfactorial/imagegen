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
from imagegen.node_registry import NodeDefinition
from imagegen.parameter import ParameterDefinition

TEST_NAME = 'TestNode'
TEST_OUTPUT = 'scalar'
TEST_INPUT = [
    ParameterDefinition('test_param',
                        param_type='scalar',
                        default_value=0.0)
]


def test_evaluation(eval_info):
    pass

TEST_DEFINITION = NodeDefinition('NodeTest', test_evaluation, TEST_INPUT, TEST_OUTPUT, None)


class TestNode(unittest.TestCase):
    def test_creation(self):
        node = Node(TEST_NAME, TEST_DEFINITION)
        self.assertIsNotNone(node)
        self.assertEqual(node.name, TEST_NAME)
        self.assertEqual(len(node.params), len(TEST_INPUT))
        self.assertEqual(0.0, node.rotation)
        self.assertEqual(node.evaluate, test_evaluation)
        self.assertEqual(node.output, TEST_OUTPUT)

    def test_read_json(self):
        pass
