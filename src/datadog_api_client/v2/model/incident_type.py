# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentType(ModelSimple):
    """
    Incident resource type.

    :param value: If omitted defaults to "incidents". Must be one of ["incidents"].
    :type value: str
    """

    allowed_values = {
        "incidents",
    }
    INCIDENTS: ClassVar["IncidentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentType.INCIDENTS = IncidentType("incidents")
