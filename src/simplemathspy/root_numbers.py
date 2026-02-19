# %%
def root(a: float, b: float) -> float:
    """Calculate the n-th root of a number.

    This function is documented in a way that mkdocstrings can
    automatically extract and render.

    Args:
        a: The number to find the root of (the radicand).
        b: The degree of the root (the index).

    Returns:
        The b-th root of a.

    Examples:
        >>> get_root(25, 2)
        5.0
        >>> get_root(8, 3)
        2.0
    """
    return a ** (1/b)
# %%


root(16,2)