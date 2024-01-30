# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogType(ModelSimple):
    """
    Type of the event.

    :param value: If omitted defaults to "log". Must be one of ["log"].
    :type value: str
    """

    allowed_values = {
        "log",
    }
    LOG: ClassVar["LogType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogType.LOG = LogType("log")