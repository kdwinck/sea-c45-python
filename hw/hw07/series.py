
def fibonacci(n):
    """
    Returns the nth number from the Fibonacci sequence.

    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    """

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Returns the nth number from the Lucas sequence.

    Example: lucas(0) == 2
             lucas(1) == 1
             ...
             lucas(n) == lucas(n - 1) + lucas(n - 2)
    """

    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """
    Returns the nth number in a sequence with a first
    number x and a second number y.

    Example: sum_series(0, 2, 3) == 2
             sum_series(5, 0, 1) == 5
             ...
             sum_series(n) == sum_series(n - 1) + sum_series(n - 2)
    """

    if (n == 0):
        return x
    elif (n == 1):
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
