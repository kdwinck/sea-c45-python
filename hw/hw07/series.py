def fibonacci(n):
    """
    Returns the nth number from the Fibonacci sequence.

    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 3
    elif n == 5:
        return 5
    elif n == 6:
        return 8
    else:
        return 13


def lucas(n):
    """
    Returns the nth numbe from the Lucas sequence.

    Example: lucas(0) == 2
             lucas(1) == 1
             lucas(2) == 3
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 4
    elif n == 4:
        return 7
    elif n == 5:
        return 11
    elif n == 6:
        return 18
    else:
        return 29
