# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsArchiveDestinationGCSType(ModelSimple):
    """
    Type of the GCS archive destination.

    :param value: If omitted defaults to "gcs". Must be one of ["gcs"].
    :type value: str
    """

    allowed_values = {
        "gcs",
    }
    GCS: ClassVar["LogsArchiveDestinationGCSType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsArchiveDestinationGCSType.GCS = LogsArchiveDestinationGCSType("gcs")