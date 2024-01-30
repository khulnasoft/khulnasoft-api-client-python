# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData


class RelationshipToUsers(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData

        return {
            "data": ([RelationshipToUserData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[RelationshipToUserData], **kwargs):
        """
        Relationship to users.

        :param data: Relationships to user objects.
        :type data: [RelationshipToUserData]
        """
        super().__init__(kwargs)

        self_.data = data
