# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_pipelines_bucket_response import CIAppPipelinesBucketResponse


class CIAppPipelinesAggregationBucketsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_pipelines_bucket_response import CIAppPipelinesBucketResponse

        return {
            "buckets": ([CIAppPipelinesBucketResponse],),
        }

    attribute_map = {
        "buckets": "buckets",
    }

    def __init__(self_, buckets: Union[List[CIAppPipelinesBucketResponse], UnsetType] = unset, **kwargs):
        """
        The query results.

        :param buckets: The list of matching buckets, one item per bucket.
        :type buckets: [CIAppPipelinesBucketResponse], optional
        """
        if buckets is not unset:
            kwargs["buckets"] = buckets
        super().__init__(kwargs)
