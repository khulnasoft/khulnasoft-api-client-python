# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UserTeamTeamType(ModelSimple):
    """
    User team team type

    :param value: If omitted defaults to "team". Must be one of ["team"].
    :type value: str
    """

    allowed_values = {
        "team",
    }
    TEAM: ClassVar["UserTeamTeamType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UserTeamTeamType.TEAM = UserTeamTeamType("team")