# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.active_billing_dimensions_body import ActiveBillingDimensionsBody


class ActiveBillingDimensionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.active_billing_dimensions_body import ActiveBillingDimensionsBody

        return {
            "data": (ActiveBillingDimensionsBody,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ActiveBillingDimensionsBody, UnsetType] = unset, **kwargs):
        """
        Active billing dimensions response.

        :param data: Active billing dimensions data.
        :type data: ActiveBillingDimensionsBody, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
