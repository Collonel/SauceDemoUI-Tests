Feature: SauceDemo Shopping Cart
    As a logged in user
    I want to manage items in my cart
    So that I can proceed to checkout

    Scenario: Add item to cart successfully
        Given I am logged in to SauceDemo
        When I add the first item to the cart
        And I go to the cart
        Then I should see the item in my cart