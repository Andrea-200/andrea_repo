def print_odd_numbers(start, end):
    """Prints all odd numbers in the specified range [start, end]."""
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number)

# Example usage:
start = 1
end = 20
print_odd_numbers(start, end)
