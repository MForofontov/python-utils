from typing import Any
from collections.abc import Callable
from contextlib import redirect_stdout
from functools import wraps
import logging
from logger_functions.logger import validate_logger


def redirect_output(
    file_path: str, logger: logging.Logger = None
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to redirect the standard output of a function to a specified file.

    Parameters
    ----------
    file_path : str
        The path to the file where the output should be redirected.
    logger : logging.Logger, optional
        The logger to use for logging errors (default is None).

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.

    Raises
    ------
    TypeError
        If the input function is not callable or if logger is not an instance of logging.Logger or None.
    """
    validate_logger(logger)
    if not isinstance(file_path, str):
        if logger:
            logger.error("file_path must be a string", exc_info=True)
        raise TypeError("file_path must be a string")

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
            The wrapper function that redirects the output.

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
            try:
                with open(file_path, "w") as f, redirect_stdout(f):
                    return func(*args, **kwargs)
            except Exception as e:
                message = f"Failed to redirect output: {e}"
                if logger:
                    logger.error(message, exc_info=True)
                raise RuntimeError(message)

        return wrapper

    return decorator
