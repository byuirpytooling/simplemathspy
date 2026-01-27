
def pctformat(value, decimals=2):
    """
    Format a number as a percentage string with specified decimal places.

    Parameters:
    value (float): The numeric value to format.
    decimals (int): The number of decimal places to include.

    Returns:
    str: The formatted percentage string.
    """
    format_string = "{:." + str(decimals) + "%}"
    return format_string.format(value)