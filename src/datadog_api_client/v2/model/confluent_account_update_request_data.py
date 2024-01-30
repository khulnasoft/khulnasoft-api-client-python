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
    from datadog_api_client.v2.model.confluent_account_update_request_attributes import (
        ConfluentAccountUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType


class ConfluentAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_update_request_attributes import (
            ConfluentAccountUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType

        return {
            "attributes": (ConfluentAccountUpdateRequestAttributes,),
            "type": (ConfluentAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ConfluentAccountUpdateRequestAttributes, type: ConfluentAccountType, **kwargs):
        """
        Data object for updating a Confluent account.

        :param attributes: Attributes object for updating a Confluent account.
        :type attributes: ConfluentAccountUpdateRequestAttributes

        :param type: The JSON:API type for this API. Should always be ``confluent-cloud-accounts``.
        :type type: ConfluentAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
