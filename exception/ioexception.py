try:
    with open("example.txt", "r") as file:
        data = file.read()
        print(data)
except IOError as e:
    print(f"An IOError occurred: {e}")
except OSError as e:
    print(f"An OSError occurred: {e}")
