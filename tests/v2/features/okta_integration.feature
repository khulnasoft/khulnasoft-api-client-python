@endpoint(okta-integration) @endpoint(okta-integration-v2)
Feature: Okta Integration
  Configure your Khulnasoft Okta integration directly through the Khulnasoft API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OktaIntegration" API

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Add Okta account returns "Bad Request" response
    Given new "CreateOktaAccount" request
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Add Okta account returns "Not Found" response
    Given new "CreateOktaAccount" request
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta-Prod"}, "id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Add Okta account returns "OK" response
    Given new "CreateOktaAccount" request
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "name": "Okta_Prod", "client_id": "client_id", "client_secret":"client_secret"},"id": "f749daaf-682e-4208-a38d-c9b43162c609", "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Delete Okta account returns "Bad Request" response
    Given new "DeleteOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Delete Okta account returns "Not Found" response
    Given new "DeleteOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Delete Okta account returns "OK" response
    Given new "DeleteOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Get Okta account returns "Bad Request" response
    Given new "GetOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Get Okta account returns "Not Found" response
    Given new "GetOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Get Okta account returns "OK" response
    Given there is a valid "okta_account" in the system
    And new "GetOktaAccount" request
    And request contains "account_id" parameter from "okta_account.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "okta-accounts"

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: List Okta accounts returns "Bad Request" response
    Given new "ListOktaAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: List Okta accounts returns "Not Found" response
    Given new "ListOktaAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: List Okta accounts returns "OK" response
    Given there is a valid "okta_account" in the system
    And new "ListOktaAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Update Okta account returns "Bad Request" response
    Given new "UpdateOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Update Okta account returns "Not Found" response
    Given new "UpdateOktaAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {}
    When the request is sent
    Then the response status is 404 Not Found

  @team:KhulnaSoft/saas-integrations @team:KhulnaSoft/web-integrations
  Scenario: Update Okta account returns "OK" response
    Given there is a valid "okta_account" in the system
    And new "UpdateOktaAccount" request
    And request contains "account_id" parameter from "okta_account.data.id"
    And body with value {"data": {"attributes": {"auth_method": "oauth", "domain": "https://example.okta.com/", "client_id": "client_id", "client_secret":"client_secret"}, "type": "okta-accounts"}}
    When the request is sent
    Then the response status is 200 OK
