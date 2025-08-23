from typing import Any
from collections.abc import Callable
from functools import wraps


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to cache the results of a function call.

    Parameters
    ----------
    func : Callable[..., Any]
        The function to be cached.

    Returns
    -------
    Callable[..., Any]
        A wrapper function that caches the results of the input function.
    """

    cached_results: dict[tuple[tuple[Any, ...], frozenset[tuple[str, Any]]], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to cache the results of the input function.

        Parameters
        ----------
        *args : Any
            Positional arguments to pass to the wrapped function.
        **kwargs : Any
            Keyword arguments to pass to the wrapped function.

        Returns
        -------
        Any
            The cached result of the wrapped function.

        Raises
        ------
        TypeError
            If the arguments are unhashable.
        """
        try:
            # Create a key based on the function arguments
            key: tuple[tuple[Any, ...], frozenset[tuple[str, Any]]] = (
                args,
                frozenset(kwargs.items()),
            )

            # Check if the result is already cached
            if key not in cached_results:
                # If not cached, call the function and store the result
                cached_results[key] = func(*args, **kwargs)
        except TypeError as e:
            raise TypeError(f"Unhashable arguments: {e}")

        # Return the cached result
        return cached_results[key]

    def cache_clear() -> None:
        """Public method to clear the cached results for ``func``."""
        cached_results.clear()

    setattr(wrapper, "cache_clear", cache_clear)

    return wrapper

__all__ = ['cache']
