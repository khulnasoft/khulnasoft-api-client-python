# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBasicAuthOauthROPType(ModelSimple):
    """
    The type of basic authentication to use when performing the test.

    :param value: If omitted defaults to "oauth-rop". Must be one of ["oauth-rop"].
    :type value: str
    """

    allowed_values = {
        "oauth-rop",
    }
    OAUTH_ROP: ClassVar["SyntheticsBasicAuthOauthROPType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBasicAuthOauthROPType.OAUTH_ROP = SyntheticsBasicAuthOauthROPType("oauth-rop")
