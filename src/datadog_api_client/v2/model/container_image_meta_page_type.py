# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ContainerImageMetaPageType(ModelSimple):
    """
    Type of Container Image pagination.

    :param value: If omitted defaults to "cursor_limit". Must be one of ["cursor_limit"].
    :type value: str
    """

    allowed_values = {
        "cursor_limit",
    }
    CURSOR_LIMIT: ClassVar["ContainerImageMetaPageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ContainerImageMetaPageType.CURSOR_LIMIT = ContainerImageMetaPageType("cursor_limit")
