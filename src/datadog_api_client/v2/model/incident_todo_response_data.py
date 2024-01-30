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
    from datadog_api_client.v2.model.incident_todo_attributes import IncidentTodoAttributes
    from datadog_api_client.v2.model.incident_todo_relationships import IncidentTodoRelationships
    from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType


class IncidentTodoResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_todo_attributes import IncidentTodoAttributes
        from datadog_api_client.v2.model.incident_todo_relationships import IncidentTodoRelationships
        from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType

        return {
            "attributes": (IncidentTodoAttributes,),
            "id": (str,),
            "relationships": (IncidentTodoRelationships,),
            "type": (IncidentTodoType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: IncidentTodoType,
        attributes: Union[IncidentTodoAttributes, UnsetType] = unset,
        relationships: Union[IncidentTodoRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident todo response data.

        :param attributes: Incident todo's attributes.
        :type attributes: IncidentTodoAttributes, optional

        :param id: The incident todo's ID.
        :type id: str

        :param relationships: The incident's relationships from a response.
        :type relationships: IncidentTodoRelationships, optional

        :param type: Todo resource type.
        :type type: IncidentTodoType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
