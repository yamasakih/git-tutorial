__version__ = "0.1.0"


def my_sum(a, b):
    return a + b


def my_mean(array):
    if len(array) == 0:
        raise ValueError("The array must not be empty.")
    return sum(array) / len(array)

def my_minus(a, b):
    return a - b