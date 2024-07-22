def print_even_numbers(start, end):
    """Prints all even numbers in the specified range [start, end]."""
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

# Example usage:
start = 1
end = 20
print_even_numbers(start, end)
