import pandas as pd
import pytest

from pandas_functions.all_match_series import all_match_series


def test_all_match_series_success() -> None:
    """Test the ``all_match_series`` function when all elements match."""
    # Test case 1: All elements match
    series1: pd.Series = pd.Series([1, 2, 3])
    series2: pd.Series = pd.Series([1, 2, 3, 4, 5])
    assert all_match_series(series1, series2) is True


def test_all_match_series_partial_match() -> None:
    """Test the ``all_match_series`` function when not all elements match."""
    # Test case 2: Partial match
    series1: pd.Series = pd.Series([1, 2, 6])
    series2: pd.Series = pd.Series([1, 2, 3, 4, 5])
    assert all_match_series(series1, series2) is False


def test_all_match_series_empty_series1() -> None:
    """Test with an empty ``series1``."""
    # Test case 3: Empty series1
    series1: pd.Series = pd.Series([], dtype=int)
    series2: pd.Series = pd.Series([1, 2, 3])
    assert all_match_series(series1, series2) is True


def test_all_match_series_empty_series2() -> None:
    """Test with an empty ``series2``."""
    # Test case 4: Empty series2
    series1: pd.Series = pd.Series([1, 2, 3])
    series2: pd.Series = pd.Series([], dtype=int)
    assert all_match_series(series1, series2) is False


def test_all_match_series_two_empty_series() -> None:
    """Test with both ``series1`` and ``series2`` empty."""
    # Test case 5: Both series empty
    series1: pd.Series = pd.Series([], dtype=int)
    series2: pd.Series = pd.Series([], dtype=int)
    assert all_match_series(series1, series2) is True


def test_all_match_series_strings() -> None:
    """Test the function with string values."""
    # Test case 6: String values
    series1: pd.Series = pd.Series(["apple", "banana"])
    series2: pd.Series = pd.Series(["apple", "banana", "cherry"])
    assert all_match_series(series1, series2) is True


def test_all_match_series_mixed_types() -> None:
    """Test the function with mixed data types."""
    # Test case 7: Mixed data types
    series1: pd.Series = pd.Series([1, "banana", 3.14])
    series2: pd.Series = pd.Series([1, "banana", 3.14, "apple"])
    assert all_match_series(series1, series2) is True


def test_all_match_series_unhashable_elements() -> None:
    """Test the function with unhashable elements such as lists."""
    # Test case 8: Unhashable elements
    series1: pd.Series = pd.Series([[1, 2], [3, 4]])
    series2: pd.Series = pd.Series([[1, 2], [3, 4], [5, 6]])
    assert all_match_series(series1, series2) is True


def test_all_match_series_type_error_series1() -> None:
    """Ensure a ``TypeError`` is raised when ``series1`` is invalid."""
    # Test case 9: Invalid series1
    with pytest.raises(TypeError):
        all_match_series("not a series", pd.Series([1, 2, 3]))


def test_all_match_series_type_error_series2() -> None:
    """Ensure a ``TypeError`` is raised when ``series2`` is invalid."""
    # Test case 10: Invalid series2
    with pytest.raises(TypeError):
        all_match_series(pd.Series([1, 2, 3]), "not a series")
