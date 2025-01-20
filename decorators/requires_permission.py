from typing import Callable, Any, List
from functools import wraps
import logging

def requires_permission(permission: str, logger: logging.Logger = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator to enforce that a user has a specific permission before executing a function.

    Parameters
    ----------
    permission : str
        The required permission that the user must have.
    logger : logging.Logger, optional
        The logger to use for logging errors (default is None).

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator function.

    Raises
    ------
    TypeError
        If logger is not an instance of logging.Logger or None.
    """
    if not isinstance(logger, logging.Logger) and logger is not None:
        raise TypeError("logger must be an instance of logging.Logger or None")
    if not isinstance(permission, str):
        if logger:
            logger.error("Type error in requires_permission decorator: permission must be a string", exc_info=True)
        raise TypeError("permission must be a string")

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
        def wrapper(user_permissions: List[str], *args: Any, **kwargs: Any) -> Any:
            """
            The wrapper function that checks for the required permission.

            Parameters
            ----------
            user_permissions : List[str]
                The list of permissions that the user has.
            *args : Any
                Positional arguments for the decorated function.
            **kwargs : Any
                Keyword arguments for the decorated function.

            Returns
            -------
            Any
                The result of the decorated function.

            Raises
            ------
            PermissionError
                If the user does not have the required permission.
            TypeError
                If user_permissions is not a list.
            """
            # Check if user_permissions is a list
            if not isinstance(user_permissions, list):
                error_message = "user_permissions must be a list."
                if logger:
                    logger.error(f"Type error in {func.__name__}: {error_message}", exc_info=True)
                raise TypeError(error_message)

            # Check if the required permission is in the user's permissions
            if permission not in user_permissions:
                error_message = f"User does not have the required permission. Required permission: {permission}, User permissions: {user_permissions}"
                if logger:
                    logger.error(f"Permission error in {func.__name__}: {error_message}", exc_info=True)
                raise PermissionError(error_message)
            # Call the original function with the provided arguments and keyword arguments
            return func(*args, **kwargs)
        return wrapper
    return decorator