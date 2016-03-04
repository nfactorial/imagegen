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


class TestParameterDefinition(unittest.TestCase):
    def test_invalid_type(self):
        self.assertRaises(TypeError, ParameterDefinition, TEST_DEFINITION_NAME)
        self.assertRaises(TypeError, ParameterDefinition, TEST_DEFINITION_NAME, param_type=TEST_INVALID_TYPE)

    def test_integer(self):
        try:
            ParameterDefinition(TEST_DEFINITION_NAME, param_type="int")
        except TypeError:
            self.fail('Parameter raised exception unexpectedly for integer type.')

    def test_scalar(self):
        try:
            ParameterDefinition(TEST_DEFINITION_NAME, param_type="scalar")
        except TypeError:
            self.fail('Parameter raised exception unexpectedly for scalar type.')

    def test_color(self):
        try:
            ParameterDefinition(TEST_DEFINITION_NAME, param_type="color")
        except TypeError:
            self.fail('Parameter raised exception unexpectedly for color type.')


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


class TestParameter(unittest.TestCase):
    def setUp(self):
        try:
            self.definition = ParameterDefinition(TEST_DEFINITION_NAME, param_type='scalar')
        except TypeError:
            self.fail('Unexpected exception when creating parameter definition for scalar type.')
        self.parameter = None

    def test_no_range(self):
        self.parameter = Parameter(self.definition)
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertFalse(self.parameter.has_range)
