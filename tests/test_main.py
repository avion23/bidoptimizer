import pytest
from src.main import add_numbers

def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
