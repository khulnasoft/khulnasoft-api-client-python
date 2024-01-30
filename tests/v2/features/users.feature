@endpoint(users) @endpoint(users-v2)
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Create a user returns "Bad Request" response
    Given new "CreateUser" request
    And body with value {"data": {"attributes": {"email": "jane.doe@example.com"}, "relationships": {"roles": {"data": [{"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}]}}, "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Create a user returns "OK" response
    Given new "CreateUser" request
    And body with value {"data": {"type": "users", "attributes": {"name": "Khulnasoft API Client Python", "email": "{{ unique }}@khulnasoft.com"}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.email" is equal to "{{ unique_lower }}@khulnasoft.com"
    And the response "data.attributes.name" is equal to "Khulnasoft API Client Python"
    And the response "data.attributes.disabled" is false
    And the response "data.attributes.service_account" is false

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Disable a user returns "Not found" response
    Given new "DisableUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Disable a user returns "OK" response
    Given there is a valid "user" in the system
    And new "DisableUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Get a user invitation returns "Not found" response
    Given new "GetInvitation" request
    And request contains "user_invitation_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Get a user invitation returns "OK" response
    Given there is a valid "user" in the system
    And the "user" has a "user_invitation"
    And new "GetInvitation" request
    And request contains "user_invitation_uuid" parameter from "user_invitation.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.invite_type" is equal to "openid_invite"
    And the response "data.attributes.uuid" is equal to "{{user_invitation.id}}"

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Get a user organization returns "Not found" response
    Given new "ListUserOrganizations" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Get a user organization returns "OK" response
    Given new "ListUserOrganizations" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Get a user permissions returns "Not found" response
    Given new "ListUserPermissions" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Get a user permissions returns "OK" response
    Given there is a valid "user" in the system
    And new "ListUserPermissions" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Get user details returns "Not found" response
    Given new "GetUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Get user details returns "OK" response
    Given there is a valid "user" in the system
    And new "GetUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK for get user
    And the response "data.id" is equal to "{{ user.data.id }}"
    And the response "data.type" is equal to "users"
    And the response "data.attributes.handle" is equal to "{{ unique_lower }}@khulnasoft.com"

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: List all users returns "Bad Request" response
    Given new "ListUsers" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:KhulnaSoft/team-aaa-identity
  Scenario: List all users returns "OK" response
    Given there is a valid "user" in the system
    And new "ListUsers" request
    And request contains "filter" parameter from "user.data.attributes.email"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_filtered_count" is equal to 1
    And the response "data[0].attributes.email" has the same value as "user.data.attributes.email"

  @replay-only @skip-validation @team:KhulnaSoft/team-aaa-identity @with-pagination
  Scenario: List all users returns "OK" response with pagination
    Given new "ListUsers" request
    And request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Send invitation emails returns "Bad Request" response
    Given new "SendInvitations" request
    And body with value {"data": []}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Send invitation emails returns "OK" response
    Given there is a valid "user" in the system
    And new "SendInvitations" request
    And body with value {"data": [{"type": "user_invitations", "relationships": {"user": {"data": {"type": "{{ user.data.type }}", "id": "{{ user.data.id }}"}}}}]}
    When the request is sent
    Then the response status is 201 OK
    And the response "data" has length 1
    And the response "data[0].attributes.invite_type" is equal to "openid_invite"

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Update a user returns "Bad Request" response
    Given new "UpdateUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "id": "00000000-0000-feed-0000-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Update a user returns "Bad User ID in Request" response
    Given there is a valid "user" in the system
    And new "UpdateUser" request
    And request contains "user_id" parameter from "user.data.id"
    And body with value {"data": {"id": "00000000-mismatch-body-id-ffffffffffff", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 422 Bad User ID in Request

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Update a user returns "Not found" response
    Given new "UpdateUser" request
    And request contains "user_id" parameter with value "00000000-dead-beef-dead-ffffffffffff"
    And body with value {"data": {"id": "00000000-dead-beef-dead-ffffffffffff", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 404 Not found

  @team:KhulnaSoft/team-aaa-identity
  Scenario: Update a user returns "OK" response
    Given there is a valid "user" in the system
    And new "UpdateUser" request
    And request contains "user_id" parameter from "user.data.id"
    And body with value {"data": {"id": "{{ user.data.id }}", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.email" has the same value as "user.data.attributes.email"
    And the response "data.attributes.title" has the same value as "user.data.attributes.title"
    And the response "data.attributes.name" is equal to "updated"
    And the response "data.attributes.disabled" is equal to true

  @generated @skip @team:KhulnaSoft/team-aaa-identity
  Scenario: Update a user returns "Unprocessable Entity" response
    Given new "UpdateUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "id": "00000000-0000-feed-0000-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
