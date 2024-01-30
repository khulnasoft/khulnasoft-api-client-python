# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class APIKeysResponseMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(self_, total_filtered_count: Union[int, UnsetType] = unset, **kwargs):
        """
        Additional information related to the API keys response.

        :param total_filtered_count: Total filtered application key count.
        :type total_filtered_count: int, optional
        """
        if total_filtered_count is not unset:
            kwargs["total_filtered_count"] = total_filtered_count
        super().__init__(kwargs)
