# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricContentEncoding(ModelSimple):
    """
    HTTP header used to compress the media-type.

    :param value: If omitted defaults to "deflate". Must be one of ["deflate", "gzip"].
    :type value: str
    """

    allowed_values = {
        "deflate",
        "gzip",
    }
    DEFLATE: ClassVar["MetricContentEncoding"]
    GZIP: ClassVar["MetricContentEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricContentEncoding.DEFLATE = MetricContentEncoding("deflate")
MetricContentEncoding.GZIP = MetricContentEncoding("gzip")
