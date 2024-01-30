# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019-Present Khulnasoft, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_incident_impact_data import RelationshipToIncidentImpactData


class RelationshipToIncidentImpacts(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_impact_data import RelationshipToIncidentImpactData

        return {
            "data": ([RelationshipToIncidentImpactData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[RelationshipToIncidentImpactData], **kwargs):
        """
        Relationship to impacts.

        :param data: An array of incident impacts.
        :type data: [RelationshipToIncidentImpactData]
        """
        super().__init__(kwargs)

        self_.data = data
