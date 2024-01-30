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
    from datadog_api_client.v2.model.azure_uc_config_patch_request_attributes import AzureUCConfigPatchRequestAttributes
    from datadog_api_client.v2.model.azure_uc_config_patch_request_type import AzureUCConfigPatchRequestType


class AzureUCConfigPatchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_uc_config_patch_request_attributes import (
            AzureUCConfigPatchRequestAttributes,
        )
        from datadog_api_client.v2.model.azure_uc_config_patch_request_type import AzureUCConfigPatchRequestType

        return {
            "attributes": (AzureUCConfigPatchRequestAttributes,),
            "type": (AzureUCConfigPatchRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AzureUCConfigPatchRequestAttributes, type: AzureUCConfigPatchRequestType, **kwargs):
        """
        Azure config Patch data.

        :param attributes: Attributes for Azure config Patch Request.
        :type attributes: AzureUCConfigPatchRequestAttributes

        :param type: Type of Azure config Patch Request.
        :type type: AzureUCConfigPatchRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
