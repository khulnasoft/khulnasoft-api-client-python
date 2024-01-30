# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMSortOrder(ModelSimple):
    """
    The order to use, ascending or descending.

    :param value: Must be one of ["asc", "desc"].
    :type value: str
    """

    allowed_values = {
        "asc",
        "desc",
    }
    ASCENDING: ClassVar["RUMSortOrder"]
    DESCENDING: ClassVar["RUMSortOrder"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMSortOrder.ASCENDING = RUMSortOrder("asc")
RUMSortOrder.DESCENDING = RUMSortOrder("desc")
