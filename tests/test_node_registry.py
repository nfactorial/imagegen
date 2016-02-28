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
