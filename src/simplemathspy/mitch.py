def duplicate_mitch(x: int) -> str:
    """
    Repeat the string 'mitch' a specified number of times.

    Args:
        x (int): The number of times to repeat 'mitch'. Must be a non-negative integer.

    Returns:
        str: A string consisting of 'mitch' repeated `x` times.

    Example:
        >>> duplicate_mitch(3)
        'mitchmitchmitch'
    """
    return 'mitch' * x
