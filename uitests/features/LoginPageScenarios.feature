Feature: Login page scenarios

  Scenario Outline: I verify that login page is displayed properly
    Given I access "https://sandbox-dashboard.primer.io/login" with <browser>
    Then  I verify page is displayed properly
    And   I quit the driver

    Examples: Browsers
      | browser |
      | Chrome  |
      | Firefox |

  Scenario Outline: I try to login with invalid user
    Given I access "https://sandbox-dashboard.primer.io/login" with <browser>
    And   I send "James" as username and "Bond" as password
    And   I click login
    Then  I get incorrect credentials warning
    And   I quit the driver

    Examples: Browsers
      | browser |
      | Chrome  |
      | Firefox |

  Scenario Outline: I try to reset my password
    Given I access "https://sandbox-dashboard.primer.io/login" with <browser>
    And   I click Forgot password
    And   I provide "someone@example.com" as email and proceed
    Then  I verify reset email sent message
    And   I quit the driver

    Examples: Browsers
      | browser |
      | Chrome  |
      | Firefox |