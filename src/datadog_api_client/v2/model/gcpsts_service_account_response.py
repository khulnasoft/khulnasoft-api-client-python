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
    from datadog_api_client.v2.model.gcpsts_service_account import GCPSTSServiceAccount


class GCPSTSServiceAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcpsts_service_account import GCPSTSServiceAccount

        return {
            "data": (GCPSTSServiceAccount,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[GCPSTSServiceAccount, UnsetType] = unset, **kwargs):
        """
        The account creation response.

        :param data: Info on your service account.
        :type data: GCPSTSServiceAccount, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
