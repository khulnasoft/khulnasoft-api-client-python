# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.bulk_mute_findings_response_data import BulkMuteFindingsResponseData


class BulkMuteFindingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_mute_findings_response_data import BulkMuteFindingsResponseData

        return {
            "data": (BulkMuteFindingsResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: BulkMuteFindingsResponseData, **kwargs):
        """
        The expected response schema.

        :param data: Data object containing the ID of the request that was updated.
        :type data: BulkMuteFindingsResponseData
        """
        super().__init__(kwargs)

        self_.data = data
