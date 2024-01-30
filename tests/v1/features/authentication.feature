@endpoint(authentication) @endpoint(authentication-v1)
Feature: Authentication
  All requests to Khulnasoft’s API must be authenticated. Requests that write
  data require reporting access and require an `API key`. Requests that read
  data require full access and also require an `application key`.  **Note:**
  All Khulnasoft API clients are configured by default to consume Khulnasoft US
  site APIs. If you are on the Khulnasoft EU site, set the environment variable
  `KHULNASOFT_HOST` to `https://api.khulnasoft.eu` or override this value
  directly when creating your client.  [Manage your account’s API and
  application keys](https://app.khulnasoft.com/organization-settings/) in
  Khulnasoft, and see the [API and Application Keys
  page](https://docs.khulnasoft.com/account_management/api-app-keys/) in the
  documentation.

  Background:
    Given an instance of "Authentication" API
    And new "Validate" request

  @skip-validation @team:KhulnaSoft/credentials-management
  Scenario: Validate API key returns "Forbidden" response
    When the request is sent
    Then the response status is 403 OK

  @team:KhulnaSoft/credentials-management
  Scenario: Validate API key returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    When the request is sent
    Then the response status is 200 OK
    And the response "valid" is equal to true
