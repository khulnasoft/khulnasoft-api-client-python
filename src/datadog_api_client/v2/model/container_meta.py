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
    from datadog_api_client.v2.model.container_meta_page import ContainerMetaPage


class ContainerMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_meta_page import ContainerMetaPage

        return {
            "pagination": (ContainerMetaPage,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    def __init__(self_, pagination: Union[ContainerMetaPage, UnsetType] = unset, **kwargs):
        """
        Response metadata object.

        :param pagination: Paging attributes.
        :type pagination: ContainerMetaPage, optional
        """
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
