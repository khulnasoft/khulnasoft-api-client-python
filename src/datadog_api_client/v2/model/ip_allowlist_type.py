# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IPAllowlistType(ModelSimple):
    """
    IP allowlist type.

    :param value: If omitted defaults to "ip_allowlist". Must be one of ["ip_allowlist"].
    :type value: str
    """

    allowed_values = {
        "ip_allowlist",
    }
    IP_ALLOWLIST: ClassVar["IPAllowlistType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IPAllowlistType.IP_ALLOWLIST = IPAllowlistType("ip_allowlist")
