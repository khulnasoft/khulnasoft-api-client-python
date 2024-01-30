# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostAttributionTagNames(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return ([str],)

    _nullable = True

    def __init__(self_, **kwargs):
        """
        Tag keys and values.
        A ``null`` value here means that the requested tag breakdown cannot be applied because it does not match the `tags
        configured for usage attribution <https://docs.khulnasoft.com/account_management/billing/usage_attribution/#getting-started>`_.
        In this scenario the API returns the total cost, not broken down by tags.
        """
        super().__init__(kwargs)
