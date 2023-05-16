__version__ = "0.1.0"


def my_sum(a, b):
    """Add two numbers together.

    Args:
        a (numeric): The first number.
        b (numeric): The second number.

    Returns:
        numeric: The sum of the two numbers.
    """
    return a + b


def my_mean(array):
    """Calculate average of numbers

    Args:
        array (List[Union[int, float]]): The array of numbers.

    Raises:
        ValueError: If the array is empty.

    Returns:
        float: The average of the numbers.
    """
    if len(array) == 0:
        raise ValueError("The array must not be empty.")
    return sum(array) / len(array)

def my_minus(a, b):
    """Subtract a from b.

    Args:
        a (numeric): The first number.
        b (numeric): The second number.

    Returns:
        numeric: The result of subtracting b from a.
    """
    return a - b