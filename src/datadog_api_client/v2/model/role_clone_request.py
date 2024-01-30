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
    from datadog_api_client.v2.model.role_clone import RoleClone


class RoleCloneRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role_clone import RoleClone

        return {
            "data": (RoleClone,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RoleClone, **kwargs):
        """
        Request to create a role by cloning an existing role.

        :param data: Data for the clone role request.
        :type data: RoleClone
        """
        super().__init__(kwargs)

        self_.data = data