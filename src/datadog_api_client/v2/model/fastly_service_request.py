# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData


class FastlyServiceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData

        return {
            "data": (FastlyServiceData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FastlyServiceData, **kwargs):
        """
        Payload schema for Fastly service requests.

        :param data: Data object for Fastly service requests.
        :type data: FastlyServiceData
        """
        super().__init__(kwargs)

        self_.data = data