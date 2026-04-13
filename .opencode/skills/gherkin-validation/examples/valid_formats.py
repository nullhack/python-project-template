"""Examples of valid BDD docstring formats."""


def test_preferred_example_format():
    """
    Example: User authentication with valid credentials
    Given: A registered user exists in the system
    When: Valid login credentials are submitted
    Then: Access should be granted to the application
    And: User session should be created
    """
    pass


def test_scenario_format_acceptable():
    """
    Scenario: Invalid login attempt
    Given: A user with incorrect credentials
    When: Login is attempted with wrong password
    Then: Access should be denied
    And: Error message should be displayed
    But: No session should be created
    """
    pass


def test_feature_format_acceptable():
    """
    Feature: Password reset functionality
    Scenario: User requests password reset
    Given: A registered user with forgotten password
    When: Password reset is requested via email
    Then: Reset email should be sent
    And: Temporary reset token should be generated
    """
    pass


def test_minimal_given_when_then():
    """
    Given: A calculator instance
    When: Division by zero is attempted
    Then: ZeroDivisionError should be raised
    """
    pass


def test_extended_gherkin_keywords():
    """
    Background: User authentication system is configured

    Example: Successful password change
    Given: An authenticated user session exists
    And: Current password is known
    When: User submits new valid password
    Then: Password should be updated in database
    And: Confirmation email should be sent
    But: Old password should no longer work
    """
    pass


def test_business_rule_format():
    """
    Rule: Users must verify email before account activation

    Example: Email verification success
    Given: User has registered with valid email
    When: Verification link is clicked within 24 hours
    Then: Account should be activated
    And: User should be redirected to dashboard
    """
    pass


def test_multiple_examples_in_outline():
    """
    Scenario Outline: User login with different credentials
    Given: A user account exists with <username>
    When: Login attempted with <password>
    Then: Result should be <outcome>

    Examples:
    | username | password | outcome |
    | john     | secret   | success |
    | jane     | wrong    | failure |
    """
    pass
