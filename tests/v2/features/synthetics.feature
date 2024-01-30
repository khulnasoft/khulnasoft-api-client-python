@endpoint(synthetics) @endpoint(synthetics-v2)
Feature: Synthetics
  Khulnasoft Synthetics uses simulated user requests and browser rendering to
  help you ensure uptime, identify regional issues, and track your
  application performance. Khulnasoft Synthetics tests come in two different
  flavors, [API tests](https://docs.khulnasoft.com/synthetics/api_tests/) and
  [browser tests](https://docs.khulnasoft.com/synthetics/browser_tests). You
  can use Khulnasoft’s API to manage both test types programmatically.  For
  more information about Synthetics, see the [Synthetics
  overview](https://docs.khulnasoft.com/synthetics/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Synthetics" API

  @team:KhulnaSoft/synthetics-app
  Scenario: Get the on-demand concurrency cap returns "OK" response
    Given new "GetOnDemandConcurrencyCap" request
    When the request is sent
    Then the response status is 200 OK

  @team:KhulnaSoft/synthetics-app
  Scenario: Save new value for on-demand concurrency cap returns "OK" response
    Given new "SetOnDemandConcurrencyCap" request
    And body with value {"on_demand_concurrency_cap": 20}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.on_demand_concurrency_cap" is equal to 20