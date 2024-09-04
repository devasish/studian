def factorial (n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer

    Returns:
    int: Factorial of n

    Raises:
    ValueError: If n is a negative integer
    """

    if n < 0: raise ValueError("Must be a positive integer")

    f = 1
    for i in range(1, n+1): f *= i
    return f
