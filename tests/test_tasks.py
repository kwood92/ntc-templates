"""Test functions for tasks.py."""

import pytest

from tasks import sanitize_image_tag, strtobool


@pytest.mark.parametrize(
    "test_case, expected",
    [
        ("y", True),
        ("yes", True),
        ("true", True),
        ("t", True),
        ("on", True),
        ("1", True),
        ("n", False),
        ("no", False),
        ("false", False),
        ("f", False),
        ("off", False),
        ("0", False),
    ],
)
def test_strtobool(test_case, expected):
    """Test strtobool function."""
    assert strtobool(test_case) == expected


def test_strtobool_error():
    """Test generation of the error message."""
    with pytest.raises(ValueError) as excinfo:
        strtobool("invalid")
    assert "Invalid truth value invalid" in str(excinfo.value)


@pytest.mark.parametrize(
    "test_case, expected",
    [
        ("9.1.0-py3.12", "9.1.0-py3.12"),
        ("9.1.0+summit.1-py3.12", "9.1.0_summit.1-py3.12"),
        ("9.1.0+summit.1+extra", "9.1.0_summit.1_extra"),
        ("feature/branch name", "feature_branch_name"),
        (".leading-period", "_leading-period"),
        ("-leading-dash", "_leading-dash"),
    ],
)
def test_sanitize_image_tag(test_case, expected):
    """Docker tags only allow [A-Za-z0-9_.-] and must not start with . or -."""
    assert sanitize_image_tag(test_case) == expected
