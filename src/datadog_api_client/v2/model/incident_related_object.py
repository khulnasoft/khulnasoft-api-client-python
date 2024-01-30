# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRelatedObject(ModelSimple):
    """
    Object related to an incident.

    :param value: Must be one of ["users", "attachments"].
    :type value: str
    """

    allowed_values = {
        "users",
        "attachments",
    }
    USERS: ClassVar["IncidentRelatedObject"]
    ATTACHMENTS: ClassVar["IncidentRelatedObject"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRelatedObject.USERS = IncidentRelatedObject("users")
IncidentRelatedObject.ATTACHMENTS = IncidentRelatedObject("attachments")