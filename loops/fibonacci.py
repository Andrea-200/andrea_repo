def print_fibonacci(limit):
    """Prints Fibonacci numbers up to the specified limit."""
    a, b = 0, 1
    while a <= limit:
        print(a)
        a, b = b, a + b

# Example usage:
limit = 100
print_fibonacci(limit)
