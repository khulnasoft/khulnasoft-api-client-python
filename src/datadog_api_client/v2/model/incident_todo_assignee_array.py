# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class IncidentTodoAssigneeArray(ModelSimple):
    """
    Array of todo assignees.


    :type value: [IncidentTodoAssignee]
    """

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_todo_assignee import IncidentTodoAssignee

        return {
            "value": ([IncidentTodoAssignee],),
        }