import pytest
from ricardo_salazar_package_sort import thoughtful_package_sort

@pytest.mark.parametrize("width, height, length, mass, expected", [
    (100, 100, 99, 19.9, "STANDARD"),
    (1, 1, 1, 1, "STANDARD"),
    # Special - Bulky by volume
    (100, 100, 100, 1, "SPECIAL"),
    (200, 200, 200, 1, "SPECIAL"),
    # Special - Bulky by dimension
    (150, 1, 1, 1, "SPECIAL"),
    (1, 150, 1, 1, "SPECIAL"),
    (1, 1, 150, 1, "SPECIAL"),
    # Special  - Heavy
    (1, 1, 1, 20, "SPECIAL"),
    (1, 1, 1, 25, "SPECIAL"),
    # Rejected
    (100, 100, 100, 20, "REJECTED"),
    (150, 150, 150, 25, "REJECTED"),
])
def test_package_sorting(width, height, length, mass, expected):
    """Test package sorting"""
    assert thoughtful_package_sort(width, height, length, mass) == expected

@pytest.mark.parametrize("width, height, length, mass", [
    (-1, 100, 100, 10),   # Negative dimensions
    (100, -1, 100, 10),
    (100, 100, -1, 10),
    (100, 100, 100, -1),
    (0, 100, 100, 10),    # Zero dimensions
    (100, 0, 100, 10),
    (100, 100, 0, 10),
    (100, 100, 100, 0),
])
def test_invalid_inputs(width, height, length, mass):
    """Test that invalid inputs raise validation errors"""
    with pytest.raises(Exception):
        thoughtful_package_sort(width, height, length, mass) 