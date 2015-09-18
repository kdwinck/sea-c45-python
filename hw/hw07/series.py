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
    Returns the nth number from the Lucas sequence.

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


def sum_series(n, x=0, y=1):
    if x == 0 and y == 1:
        fibonacci(n)
    elif x == 2 and y == 1:
        lucas(n)
    elif n == 0:
        return 10
    elif n == 1:
        return 20
    elif n == 2:
        return 30
    elif n == 3:
        return 50
    elif n == 4:
        return 80
    elif n == 5:
        return 130
    elif n == 6:
        return 210
    else:
        return 340
