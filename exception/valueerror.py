try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError as e:
    print(f"ValueError occurred: {e}. Please enter a valid integer.")
