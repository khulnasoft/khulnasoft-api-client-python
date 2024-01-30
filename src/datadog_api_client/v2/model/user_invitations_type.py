# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UserInvitationsType(ModelSimple):
    """
    User invitations type.

    :param value: If omitted defaults to "user_invitations". Must be one of ["user_invitations"].
    :type value: str
    """

    allowed_values = {
        "user_invitations",
    }
    USER_INVITATIONS: ClassVar["UserInvitationsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UserInvitationsType.USER_INVITATIONS = UserInvitationsType("user_invitations")
