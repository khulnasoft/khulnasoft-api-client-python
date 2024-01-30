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
    from datadog_api_client.v2.model.finding_type import FindingType


class BulkMuteFindingsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_type import FindingType

        return {
            "id": (str,),
            "type": (FindingType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, type: Union[FindingType, UnsetType] = unset, **kwargs):
        """
        Data object containing the ID of the request that was updated.

        :param id: UUID used to identify the request
        :type id: str, optional

        :param type: The JSON:API type for findings.
        :type type: FindingType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
