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
    from datadog_api_client.v2.model.process_summaries_meta_page import ProcessSummariesMetaPage


class ProcessSummariesMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.process_summaries_meta_page import ProcessSummariesMetaPage

        return {
            "page": (ProcessSummariesMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[ProcessSummariesMetaPage, UnsetType] = unset, **kwargs):
        """
        Response metadata object.

        :param page: Paging attributes.
        :type page: ProcessSummariesMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
