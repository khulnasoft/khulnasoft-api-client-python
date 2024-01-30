# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentNonKhulnasoftCreator(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "image_48_px": (str,),
            "name": (str,),
        }

    attribute_map = {
        "image_48_px": "image_48_px",
        "name": "name",
    }

    def __init__(self_, image_48_px: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Incident's non Khulnasoft creator.

        :param image_48_px: Non Khulnasoft creator ``48px`` image.
        :type image_48_px: str, optional

        :param name: Non Khulnasoft creator name.
        :type name: str, optional
        """
        if image_48_px is not unset:
            kwargs["image_48_px"] = image_48_px
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
