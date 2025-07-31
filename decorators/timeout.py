import logging
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError
from typing import Any
from collections.abc import Callable
from functools import wraps
from logger_functions.logger import validate_logger


class TimeoutException(Exception):
    pass


def timeout(
    seconds: int, logger: logging.Logger | None = None
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator that enforces a timeout on a function.
    The wrapped function runs in a separate thread so this implementation works
    on all platforms, including Windows. If the timeout is reached, the
    decorated call returns ``TimeoutException`` while the original thread may
    continue running in the background.

    Parameters
    ----------
    seconds : int
        The maximum number of seconds the function is allowed to run.
    logger : Optional[logging.Logger]
        The logger to use for logging timeout messages. If None, messages are printed to the console.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.

    Raises
    ------
    TypeError
        If ``seconds`` is not an integer or if ``logger`` is not an instance of
        ``logging.Logger`` or ``None``.
    """
    validate_logger(logger)

    if not isinstance(seconds, int) or seconds < 0:
        if logger:
            logger.error(
                "Type error in timeout decorator: seconds must be a positive integer.",
                exc_info=True,
            )
        raise TypeError("seconds must be a positive integer")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        The actual decorator function.

        Parameters
        ----------
        func : Callable[..., Any]
            The function to be decorated.

        Returns
        -------
        Callable[..., Any]
            The wrapped function.
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            The wrapper function that enforces the timeout.

            Parameters
            ----------
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            Any
                The result of the decorated function.
            """

            def _run_func() -> Any:
                return func(*args, **kwargs)

            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(_run_func)
                try:
                    return future.result(timeout=seconds)
                except FuturesTimeoutError:
                    message = (
                        f"Function {func.__name__} timed out after {seconds} seconds"
                    )
                    if logger:
                        logger.error(message)
                    # Attempt to cancel but function may continue running in background
                    future.cancel()
                    raise TimeoutException(message)

        return wrapper

    return decorator

__all__ = ['TimeoutException', 'timeout']
