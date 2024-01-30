# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardInviteType(ModelSimple):
    """
    Type for shared dashboard invitation request body.

    :param value: If omitted defaults to "public_dashboard_invitation". Must be one of ["public_dashboard_invitation"].
    :type value: str
    """

    allowed_values = {
        "public_dashboard_invitation",
    }
    PUBLIC_DASHBOARD_INVITATION: ClassVar["DashboardInviteType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardInviteType.PUBLIC_DASHBOARD_INVITATION = DashboardInviteType("public_dashboard_invitation")