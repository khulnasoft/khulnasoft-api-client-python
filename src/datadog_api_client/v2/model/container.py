# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.khulnasoft.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.container_attributes import ContainerAttributes
    from datadog_api_client.v2.model.container_type import ContainerType


class Container(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_attributes import ContainerAttributes
        from datadog_api_client.v2.model.container_type import ContainerType

        return {
            "attributes": (ContainerAttributes,),
            "id": (str,),
            "type": (ContainerType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ContainerAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ContainerType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Container object.

        :param attributes: Attributes for a container.
        :type attributes: ContainerAttributes, optional

        :param id: Container ID.
        :type id: str, optional

        :param type: Type of container.
        :type type: ContainerType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
