# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_origin import MetricOrigin


class MetricMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_origin import MetricOrigin

        return {
            "origin": (MetricOrigin,),
        }

    attribute_map = {
        "origin": "origin",
    }

    def __init__(self_, origin: Union[MetricOrigin, UnsetType] = unset, **kwargs):
        """
        Metadata for the metric.

        :param origin: Metric origin information.
        :type origin: MetricOrigin, optional
        """
        if origin is not unset:
            kwargs["origin"] = origin
        super().__init__(kwargs)