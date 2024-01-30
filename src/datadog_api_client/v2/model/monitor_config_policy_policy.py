# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class MonitorConfigPolicyPolicy(ModelComposed):
    def __init__(self, **kwargs):
        """
        Configuration for the policy.

        :param tag_key: The key of the tag.
        :type tag_key: str, optional

        :param tag_key_required: If a tag key is required for monitor creation.
        :type tag_key_required: bool, optional

        :param valid_tag_values: Valid values for the tag.
        :type valid_tag_values: [str], optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.monitor_config_policy_tag_policy import MonitorConfigPolicyTagPolicy

        return {
            "oneOf": [
                MonitorConfigPolicyTagPolicy,
            ],
        }
