# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_attributes import EventAttributes


class EventResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_attributes import EventAttributes

        return {
            "attributes": (EventAttributes,),
            "message": (str,),
            "tags": ([str],),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "message": "message",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        attributes: Union[EventAttributes, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object description of an event response attribute.

        :param attributes: Object description of attributes from your event.
        :type attributes: EventAttributes, optional

        :param message: The message of the event.
        :type message: str, optional

        :param tags: An array of tags associated with the event.
        :type tags: [str], optional

        :param timestamp: The timestamp of the event.
        :type timestamp: datetime, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if message is not unset:
            kwargs["message"] = message
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
