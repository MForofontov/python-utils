from multiprocessing_functions.parallel_gather_errors import parallel_gather_errors


def risky(x: int) -> int:
    if x == 2:
        raise ValueError("bad")
    return x * x


def inc(x: int) -> int:
    return x + 1


def test_parallel_gather_errors_with_exception() -> None:
    """Test gathering errors when some inputs raise exceptions."""
    # Test case 1: Function raises error for certain values
    data: list[int] = [1, 2, 3]
    results, errors = parallel_gather_errors(risky, data)
    assert results == [1, 9]
    assert len(errors) == 1 and isinstance(errors[0], ValueError)


def test_parallel_gather_errors_no_error() -> None:
    """Test when function does not raise any exceptions."""
    # Test case 2: No errors
    data: list[int] = [1, 2, 3]
    results, errors = parallel_gather_errors(inc, data)
    assert results == [2, 3, 4]
    assert errors == []
