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
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_data import (
        CloudWorkloadSecurityAgentRuleUpdateData,
    )


class CloudWorkloadSecurityAgentRuleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_data import (
            CloudWorkloadSecurityAgentRuleUpdateData,
        )

        return {
            "data": (CloudWorkloadSecurityAgentRuleUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CloudWorkloadSecurityAgentRuleUpdateData, **kwargs):
        """
        Request object that includes the Agent rule with the attributes to update.

        :param data: Object for a single Agent rule.
        :type data: CloudWorkloadSecurityAgentRuleUpdateData
        """
        super().__init__(kwargs)

        self_.data = data