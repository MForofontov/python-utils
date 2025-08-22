import pandas as pd
from pandas_functions import concat_dfs


def test_concat_dfs_rows() -> None:
    """Test concatenating DataFrames along rows."""
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
    result = concat_dfs([df1, df2])
    expected = pd.DataFrame(
        {"A": [1, 2, 5, 6], "B": [3, 4, 7, 8]}, index=[0, 1, 0, 1]
    )
    assert result.shape == (4, 2)
    assert list(result.columns) == ["A", "B"]
    pd.testing.assert_frame_equal(result, expected)


def test_concat_dfs_columns() -> None:
    """Test concatenating DataFrames along columns."""
    df1 = pd.DataFrame({"A": [1, 2]})
    df2 = pd.DataFrame({"B": [3, 4]})
    result = concat_dfs([df1, df2], axis=1)
    expected = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    assert result.shape == (2, 2)
    assert list(result.columns) == ["A", "B"]
    pd.testing.assert_frame_equal(result, expected)
