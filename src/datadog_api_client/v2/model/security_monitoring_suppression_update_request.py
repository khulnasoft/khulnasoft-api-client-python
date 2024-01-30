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
    from datadog_api_client.v2.model.security_monitoring_suppression_update_data import (
        SecurityMonitoringSuppressionUpdateData,
    )


class SecurityMonitoringSuppressionUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_suppression_update_data import (
            SecurityMonitoringSuppressionUpdateData,
        )

        return {
            "data": (SecurityMonitoringSuppressionUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringSuppressionUpdateData, **kwargs):
        """
        Request object containing the fields to update on the suppression rule.

        :param data: The new suppression properties; partial updates are supported.
        :type data: SecurityMonitoringSuppressionUpdateData
        """
        super().__init__(kwargs)

        self_.data = data