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
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser


class IncidentTeamRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser

        return {
            "created_by": (RelationshipToUser,),
            "last_modified_by": (RelationshipToUser,),
        }

    attribute_map = {
        "created_by": "created_by",
        "last_modified_by": "last_modified_by",
    }

    def __init__(
        self_,
        created_by: Union[RelationshipToUser, UnsetType] = unset,
        last_modified_by: Union[RelationshipToUser, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident team's relationships.

        :param created_by: Relationship to user.
        :type created_by: RelationshipToUser, optional

        :param last_modified_by: Relationship to user.
        :type last_modified_by: RelationshipToUser, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if last_modified_by is not unset:
            kwargs["last_modified_by"] = last_modified_by
        super().__init__(kwargs)
