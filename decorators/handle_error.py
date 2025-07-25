from typing import Any
from collections.abc import Callable
from functools import wraps
import logging
from logger_functions.logger import validate_logger


def handle_error(
    error_message: str, logger: logging.Logger | None = None
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to handle exceptions in the decorated function. If an exception occurs,
    it logs a specified error message and returns None.

    Parameters
    ----------
    error_message : str
        The error message to log if an exception occurs.
    logger : Optional[logging.Logger]
        The logger to use for logging. If None, logging is disabled.

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.

    Raises
    ------
    TypeError
        If the logger is not an instance of logging.Logger or None.
    """
    validate_logger(logger)

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
            The wrapper function that handles exceptions.

            Parameters
            ----------
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            Any
                The result of the decorated function, or None if an exception occurs.
            """
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if logger:
                    logger.error(f"{error_message}: {e}")
                else:
                    print(f"{error_message}: {e}")
                return None

        return wrapper

    return decorator
