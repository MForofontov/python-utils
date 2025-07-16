import pytest
from multiprocessing_functions.parallel_dynamic_distribute import parallel_dynamic_distribute

def square(x: int) -> int:
    return x * x


def test_parallel_dynamic_distribute_basic() -> None:
    """Test dynamic distribution with a square function."""
    # Test case 1: Basic dynamic distribute
    data: list[int] = [1, 2, 3, 4]
    result: list[int] = parallel_dynamic_distribute(square, data, chunk_size=2)
    assert result == [1, 4, 9, 16]


def test_parallel_dynamic_distribute_empty() -> None:
    """Test dynamic distribution with an empty list."""
    # Test case 2: Empty list
    data: list[int] = []
    result: list[int] = parallel_dynamic_distribute(square, data)
    assert result == []
