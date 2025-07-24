Feature: SauceDemo Login
    As a user
    I want to login to SauceDemo
    So that I can access the inventory

    Scenario: Successful login with valid credentials
        Given I am on the login page
        When I login with valid credentials
        Then I should be redirected to the inventory page

    Scenario: Failed login with invalid credentials
        Given I am on the login page
        When I login with invalid credentials
        Then I should see an error message