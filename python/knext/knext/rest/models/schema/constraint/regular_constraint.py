# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.rest.configuration import Configuration


class RegularConstraint(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"constraint_type_enum": "str", "regular_pattern": "str"}

    attribute_map = {
        "constraint_type_enum": "constraintTypeEnum",
        "regular_pattern": "regularPattern",
    }

    def __init__(
        self,
        constraint_type_enum="REGULAR",
        regular_pattern=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """RegularConstraint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._constraint_type_enum = None
        self._regular_pattern = None
        self.discriminator = constraint_type_enum

        self.constraint_type_enum = constraint_type_enum
        if regular_pattern is not None:
            self.regular_pattern = regular_pattern

    @property
    def constraint_type_enum(self):
        """Gets the constraint_type_enum of this RegularConstraint.  # noqa: E501


        :return: The constraint_type_enum of this RegularConstraint.  # noqa: E501
        :rtype: str
        """
        return self._constraint_type_enum

    @constraint_type_enum.setter
    def constraint_type_enum(self, constraint_type_enum):
        """Sets the constraint_type_enum of this RegularConstraint.


        :param constraint_type_enum: The constraint_type_enum of this RegularConstraint.  # noqa: E501
        :type: str
        """
        allowed_values = [
            None,
            "NOT_NULL",
            "UNIQUE",
            "MULTI_VALUE",
            "ENUM",
            "RANGE",
            "REGULAR",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and constraint_type_enum not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `constraint_type_enum` ({0}), must be one of {1}".format(  # noqa: E501
                    constraint_type_enum, allowed_values
                )
            )

        self._constraint_type_enum = constraint_type_enum

    @property
    def regular_pattern(self):
        """Gets the regular_pattern of this RegularConstraint.  # noqa: E501


        :return: The regular_pattern of this RegularConstraint.  # noqa: E501
        :rtype: str
        """
        return self._regular_pattern

    @regular_pattern.setter
    def regular_pattern(self, regular_pattern):
        """Sets the regular_pattern of this RegularConstraint.


        :param regular_pattern: The regular_pattern of this RegularConstraint.  # noqa: E501
        :type: str
        """

        self._regular_pattern = regular_pattern

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegularConstraint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegularConstraint):
            return True

        return self.to_dict() != other.to_dict()
