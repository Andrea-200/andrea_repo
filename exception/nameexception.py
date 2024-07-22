class CustomError(Exception):
    """Base class for other custom exceptions."""
    pass

class ValueTooHighError(CustomError):
    """Raised when the input value is too high."""
    def __init__(self, value, message="Value is too high"):
        self.value = value
        self.message = message
        super().__init__(self.message)

class ValueTooLowError(CustomError):
    """Raised when the input value is too low."""
    def __init__(self, value, message="Value is too low"):
        self.value = value
        self.message = message
        super().__init__(self.message)

# Example usage:
def check_value(value):
    if value > 100:
        raise ValueTooHighError(value)
    elif value < 0:
        raise ValueTooLowError(value)
    else:
        print("Value is within the acceptable range.")

try:
    check_value(150)
except CustomError as e:
    print(f"CustomError occurred: {e}.")
