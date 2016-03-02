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

TEST_NAME = 'TestParameter'
TEST_INVALID_TYPE = 'invalid_type'


class TestParameterDefinition(unittest.TestCase):
    def test_invalid_type(self):
        self.assertRaises(TypeError, ParameterDefinition(TEST_NAME,
                                                         param_type=TEST_INVALID_TYPE))

    def test_integer(self):
        pass

    def test_scalar(self):
        pass

    def test_color(self):
        pass


# TODO: Test Parameter class
