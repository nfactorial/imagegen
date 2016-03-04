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

from imagegen.parameter import ParameterDefinition, Parameter

TEST_DEFINITION_NAME = 'TestDefinition'
TEST_INVALID_TYPE = 'invalid_type'
TEST_PARAMETER_NAME = 'TestParameter'


class TestInvalidParameter(unittest.TestCase):
    def test_construction(self):
        """
        Ensure the expected exceptions are raised when passing invalid arguments to the parameter definition type.
        """
        self.assertRaises(ValueError, ParameterDefinition, None)
        self.assertRaises(ValueError, ParameterDefinition, None, param_type=TEST_INVALID_TYPE)
        self.assertRaises(ValueError, ParameterDefinition, None, param_type='scalar')
        self.assertRaises(TypeError, ParameterDefinition, TEST_DEFINITION_NAME)
        self.assertRaises(TypeError, ParameterDefinition, TEST_DEFINITION_NAME, param_type=TEST_INVALID_TYPE)


class TestParameterScalar(unittest.TestCase):
    def setUp(self):
        try:
            self.definition = ParameterDefinition(TEST_DEFINITION_NAME, param_type='scalar')
        except TypeError:
            self.fail('Unexpected exception when creating parameter definition for scalar type.')
        self.parameter = Parameter(self.definition)

    def test_no_range(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual('scalar', self.parameter.type)
        self.assertFalse(self.parameter.has_range)


class TestParameterInt(unittest.TestCase):
    def setUp(self):
        try:
            self.definition = ParameterDefinition(TEST_DEFINITION_NAME, param_type='int')
        except TypeError:
            self.fail('Unexpected exception when creating parameter definition for integer type.')
        self.parameter = Parameter(self.definition)

    def test_no_range(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual('int', self.parameter.type)
        self.assertFalse(self.parameter.has_range)


class TestParameterColor(unittest.TestCase):
    def setUp(self):
        try:
            self.definition = ParameterDefinition(TEST_DEFINITION_NAME, param_type='color')
        except TypeError:
            self.fail('Unexpected exception when creating parameter definition for color type.')
        self.parameter = Parameter(self.definition)

    def test_no_range(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual('color', self.parameter.type)
        self.assertFalse(self.parameter.has_range)
