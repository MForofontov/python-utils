import pandas as pd
import pytest

from pandas_functions.convert_df_column_dtype import convert_df_column_dtype


def test_convert_df_column_dtype() -> None:
    """
    Converting a column should change its dtype.
    """
    # Test case 1: Convert str to int
    df: pd.DataFrame = pd.DataFrame({"A": ["1", "2"]})
    result: pd.DataFrame = convert_df_column_dtype(df, "A", int)
    expected: pd.DataFrame = pd.DataFrame({"A": [1, 2]})
    pd.testing.assert_frame_equal(result, expected)


def test_convert_df_column_dtype_missing() -> None:
    """
    Requesting a missing column should raise ``KeyError``.
    """
    # Test case 2: Missing column
    df: pd.DataFrame = pd.DataFrame({"A": [1]})
    with pytest.raises(KeyError):
        convert_df_column_dtype(df, "B", int)


def test_convert_df_column_dtype_invalid_df() -> None:
    """
    Ensure passing a non-DataFrame raises ``AttributeError``.
    """
    # Test case 3: Invalid DataFrame input
    with pytest.raises(AttributeError):
        convert_df_column_dtype("not a df", "A", int)
