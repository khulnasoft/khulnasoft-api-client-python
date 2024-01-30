# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBrowserTestType(ModelSimple):
    """
    Type of the Synthetic test, `browser`.

    :param value: If omitted defaults to "browser". Must be one of ["browser"].
    :type value: str
    """

    allowed_values = {
        "browser",
    }
    BROWSER: ClassVar["SyntheticsBrowserTestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBrowserTestType.BROWSER = SyntheticsBrowserTestType("browser")
