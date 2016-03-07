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

SCALAR_TYPE = 'scalar'
COLOR_TYPE = 'color'
INT_TYPE = 'int'


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


class TestParameterBase(unittest.TestCase):
    """
    Base class for all parameter unit tests, implements the creation of the
    parameter being tested.
    """
    def __init__(self,
                 methodName='runTest',
                 param_name=None,
                 param_type=None,
                 minimum=None,
                 maximum=None,
                 default_value=None):
        super(TestParameterBase, self).__init__(methodName=methodName)
        self.name = param_name
        self.param_type = param_type
        self.minimum = minimum
        self.maximum = maximum
        self.default_value = default_value
        self.definition = None
        self.parameter = None

    def setUp(self):
        try:
            self.definition = ParameterDefinition(self.name,
                                                  param_type=self.param_type,
                                                  minimum=self.minimum,
                                                  maximum=self.maximum,
                                                  default_value=self.default_value)
        except TypeError:
            self.fail("Unexpected exception when creating parameter definition for %s type." % self.param_type)
        self.parameter = Parameter(self.definition)

    def tearDown(self):
        self.definition = None
        self.parameter = None


class TestParameterScalarNoRange(TestParameterBase):
    """
    Verify behavior of scalar parameter type with no range.
    """
    def __init__(self, methodName='runTest'):
        super(TestParameterScalarNoRange, self).__init__(methodName=methodName,
                                                         param_name=TEST_DEFINITION_NAME,
                                                         param_type=SCALAR_TYPE)

    def test_no_range(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual(SCALAR_TYPE, self.parameter.type)
        self.assertFalse(self.parameter.has_range)


class TestParameterScalarRanged(TestParameterBase):
    """
    Verify behavior of ranged scalar parameter type.
    """
    def __init__(self, methodName='runTest'):
        super(TestParameterScalarRanged, self).__init__(methodName=methodName,
                                                        param_name=TEST_DEFINITION_NAME,
                                                        param_type=SCALAR_TYPE,
                                                        minimum=0.0,
                                                        maximum=1.0)

    def test_ranged(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual(SCALAR_TYPE, self.parameter.type)
        self.assertTrue(self.parameter.has_range)


class TestParameterIntNoRange(TestParameterBase):
    """
    Verify behavior of integer parameter type with no range.
    """
    def __init__(self, methodName='runTest'):
        super(TestParameterIntNoRange, self).__init__(methodName=methodName,
                                                      param_name=TEST_DEFINITION_NAME,
                                                      param_type=INT_TYPE)

    def test_no_range(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual(INT_TYPE, self.parameter.type)
        self.assertFalse(self.parameter.has_range)


class TestParameterIntRanged(TestParameterBase):
    """
    Verify behavior of ranged integer type.
    """
    def __init__(self, methodName='runTest'):
        super(TestParameterIntRanged, self).__init__(methodName=methodName,
                                                     param_name=TEST_DEFINITION_NAME,
                                                     param_type=INT_TYPE,
                                                     minimum=0.0,
                                                     maximum=1.0)

    def test_ranged(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual(INT_TYPE, self.parameter.type)
        self.assertTrue(self.parameter.has_range)


class TestParameterColor(TestParameterBase):
    """
    Verify behavior of color parameter type.
    """
    def __init__(self, methodName='runTest'):
        super(TestParameterColor, self).__init__(methodName=methodName,
                                                 param_name=TEST_DEFINITION_NAME,
                                                 param_type=COLOR_TYPE)

    def test_creation(self):
        self.assertEqual(TEST_DEFINITION_NAME, self.parameter.name)
        self.assertEqual(COLOR_TYPE, self.parameter.type)
        self.assertFalse(self.parameter.has_range)
