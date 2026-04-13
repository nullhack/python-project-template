"""Examples of invalid BDD docstring formats that need correction."""


def test_missing_newlines_invalid():
    """Example: Missing proper newlines
    Given: Newlines are required
    When: Format is checked
    Then: Should fail validation"""
    # INVALID: Missing starting and ending newlines
    pass


def test_empty_keywords_invalid():
    """
    Example: Empty keyword content
    Given:
    When:
    Then:
    """
    # INVALID: Keywords have no content
    pass


def test_no_gherkin_keywords_invalid():
    """
    This test checks user login functionality.
    It should validate credentials and grant access.
    """
    # INVALID: No Gherkin keywords at all
    pass


def test_invalid_keywords_wrong():
    """
    Setup: System is initialized
    Action: User performs login
    Result: Access is granted
    """
    # INVALID: Using non-Gherkin keywords
    pass


def test_missing_colons_invalid():
    """
    Example Missing colon after keyword
    Given User has valid credentials
    When Login is submitted
    Then Access should be granted
    """
    # INVALID: Missing colons after keywords
    pass


def test_incomplete_structure_issues():
    """
    Example: Incomplete test scenario
    Given: User exists in system
    # Missing When and Then
    """
    # INVALID: Incomplete Given/When/Then structure
    pass


def test_mixed_invalid_and_valid():
    """
    Example: Mixed format with issues
    Given: Valid precondition exists
    Setup: Invalid keyword here
    When: Action is performed
    Then: Expected outcome occurs
    """
    # INVALID: Mixing valid and invalid keywords
    pass


def test_no_docstring_at_all():
    # INVALID: Completely missing docstring
    pass
