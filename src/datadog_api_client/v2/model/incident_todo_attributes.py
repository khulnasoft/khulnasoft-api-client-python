# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray


class IncidentTodoAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray

        return {
            "assignees": (IncidentTodoAssigneeArray,),
            "completed": (str, none_type),
            "content": (str,),
            "created": (datetime,),
            "due_date": (str, none_type),
            "incident_id": (str,),
            "modified": (datetime,),
        }

    attribute_map = {
        "assignees": "assignees",
        "completed": "completed",
        "content": "content",
        "created": "created",
        "due_date": "due_date",
        "incident_id": "incident_id",
        "modified": "modified",
    }
    read_only_vars = {
        "created",
        "modified",
    }

    def __init__(
        self_,
        assignees: IncidentTodoAssigneeArray,
        content: str,
        completed: Union[str, none_type, UnsetType] = unset,
        created: Union[datetime, UnsetType] = unset,
        due_date: Union[str, none_type, UnsetType] = unset,
        incident_id: Union[str, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident todo's attributes.

        :param assignees: Array of todo assignees.
        :type assignees: IncidentTodoAssigneeArray

        :param completed: Timestamp when the todo was completed.
        :type completed: str, none_type, optional

        :param content: The follow-up task's content.
        :type content: str

        :param created: Timestamp when the incident todo was created.
        :type created: datetime, optional

        :param due_date: Timestamp when the todo should be completed by.
        :type due_date: str, none_type, optional

        :param incident_id: UUID of the incident this todo is connected to.
        :type incident_id: str, optional

        :param modified: Timestamp when the incident todo was last modified.
        :type modified: datetime, optional
        """
        if completed is not unset:
            kwargs["completed"] = completed
        if created is not unset:
            kwargs["created"] = created
        if due_date is not unset:
            kwargs["due_date"] = due_date
        if incident_id is not unset:
            kwargs["incident_id"] = incident_id
        if modified is not unset:
            kwargs["modified"] = modified
        super().__init__(kwargs)

        self_.assignees = assignees
        self_.content = content
