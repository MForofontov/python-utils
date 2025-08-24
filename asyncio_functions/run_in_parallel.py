from typing import TypeVar, Awaitable
from collections.abc import Callable
import asyncio

T = TypeVar("T")


async def run_in_parallel(tasks: list[Callable[..., Awaitable[T]]]) -> list[T]:
    """
    Run multiple asynchronous functions in parallel.

    Parameters
    ----------
    tasks : list[Callable[..., Awaitable[T]]]
        A list of asynchronous functions to execute.

    Returns
    -------
    List[T]
        A list of results from the asynchronous functions.

    Raises
    ------
    TypeError
        If any item in ``tasks`` is not a callable that returns an awaitable.
    Exception
        Propagates any exception raised by the executed tasks.

    Examples
    --------
    >>> async def task_a() -> str:
    >>>     await asyncio.sleep(1)
    >>>     return "Task A done"
    >>> async def task_b() -> str:
    >>>     await asyncio.sleep(2)
    >>>     return "Task B done"
    >>> asyncio.run(run_in_parallel([task_a, task_b]))
    ['Task A done', 'Task B done']
    """
    task_list = [task() for task in tasks]  # Start all tasks concurrently
    return await asyncio.gather(*task_list)

__all__ = ['run_in_parallel']
