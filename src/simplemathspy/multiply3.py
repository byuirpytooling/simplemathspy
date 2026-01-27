
def multiply3(a: float, b: float, c: float) -> float:
    """Multiply three numbers together.

    This function is documented in a way that mkdocstrings can
    automatically extract and render.

    Args:
      a: float The first number to multiply.
      b: float The second number to multiply.
      c: float The third number to multiply.

    Returns:
      float The product of ``a``, ``b``, and ``c``.

    Examples:
        >>> multiply3(2, 3, 4)
        24
        >>> multiply3(-1.5, 0.5, 2)
        -3.0
    """
    return a * b * c
