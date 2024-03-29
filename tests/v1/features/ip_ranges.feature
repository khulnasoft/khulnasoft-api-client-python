@endpoint(ip-ranges) @endpoint(ip-ranges-v1)
Feature: IP Ranges
  Get a list of IP prefixes belonging to Khulnasoft.

  @team:KhulnaSoft/network-edge
  Scenario: List IP Ranges returns "OK" response
    Given an instance of "IPRanges" API
    And new "GetIPRanges" request
    When the request is sent
    Then the response status is 200 OK
    And the response "agents.prefixes_ipv4" has length 1
    And the response "agents.prefixes_ipv6" has length 1
