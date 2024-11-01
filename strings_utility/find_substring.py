def find_substring(s: str, substring: str) -> int:
    """
    Find the first occurrence of a substring in a string.

    Parameters
    ----------
    s : str
        The input string.
    substring : str
        The substring to find.

    Returns
    -------
    int
        The index of the first occurrence of the substring, or -1 if not found.

    Examples
    --------
    >>> find_substring("hello world", "world")
    6
    >>> find_substring("hello world", "there")
    -1
    """
    if not isinstance(s, str) or not isinstance(substring, str):
        raise TypeError("The input must be a string.")
    return s.find(substring)
