def add_fourteen(x: int) -> int:
    """Add fourteen to an integer.

    This function takes an integer input and returns the result
    of adding 14 to it. The documentation format is compatible
    with mkdocstrings.

    Args:
      x: int The integer to which 14 will be added.

    Returns:
      int The result of ``x + 14``.

    Examples:
        >>> add_fourteen(0)
        14
        >>> add_fourteen(6)
        20
        >>> add_fourteen(-4)
        10
    """
    return x + 14