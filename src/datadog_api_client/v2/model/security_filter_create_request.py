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
    from datadog_api_client.v2.model.security_filter_create_data import SecurityFilterCreateData


class SecurityFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_create_data import SecurityFilterCreateData

        return {
            "data": (SecurityFilterCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityFilterCreateData, **kwargs):
        """
        Request object that includes the security filter that you would like to create.

        :param data: Object for a single security filter.
        :type data: SecurityFilterCreateData
        """
        super().__init__(kwargs)

        self_.data = data