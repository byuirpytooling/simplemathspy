# %%
def bad_multiply(a: int, b: int) -> int:
    """Multiplies two numbers together slowly

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: result of a * b

    Examples:
        >>> bad_multiply(3, 5)
        15
        >>> bad_multiply(-2, -2)
        4
    """

    if a == 0 or b == 0:
        return 0

    result = 0
    for i in range(abs(b)):
        result += a

    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = abs(result) * -1
    else:
        result = abs(result)


    return result

# %%