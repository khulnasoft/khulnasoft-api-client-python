from khulnasoft_api_client.v1.model.monitor_thresholds import MonitorThresholds
from khulnasoft_api_client.v2.model.logs_group_by import LogsGroupBy
from khulnasoft_api_client.v2.model.logs_group_by_missing import LogsGroupByMissing
from khulnasoft_api_client.v2.model.logs_group_by_total import LogsGroupByTotal
from khulnasoft_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort
from khulnasoft_api_client.v2.model.logs_aggregate_sort_type import LogsAggregateSortType
from khulnasoft_api_client.v2.model.logs_aggregation_function import LogsAggregationFunction
from khulnasoft_api_client.v2.model.logs_sort_order import LogsSortOrder


def test_default_coerce():
    thresholds = MonitorThresholds(critical=5)
    assert thresholds["critical"] == 5.0


def test_primitive_one_of():
    group_by = LogsGroupBy(
        facet="host",
        missing=LogsGroupByMissing("miss"),
        sort=LogsAggregateSort(
            type=LogsAggregateSortType("measure"),
            order=LogsSortOrder("asc"),
            aggregation=LogsAggregationFunction("pc90"),
            metric="@duration",
        ),
        total=LogsGroupByTotal("recall"),
    )

    assert group_by.missing == "miss"
