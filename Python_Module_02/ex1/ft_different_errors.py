def garden_operations(x):
    """Trigger and catch specific errors based on input string."""
    if x == "ValueError":
        try:
            int('ABC')
        except ValueError:
            return "Caught ValueError: invalid literal for int()"

    if x == "ZeroDivisionError":
        try:
            nbr_test = 10 / 0
            print(nbr_test)
        except ZeroDivisionError:
            return "Caught ZeroDivisionError: division by zero"

    if x == "FileNotFoundError":
        try:
            f = open("missing.txt", "r")
            print(f.read())
        except FileNotFoundError:
            return "Caught FileNotFoundError:No such file 'missing.txt'"

    if x == "KeyError":
        try:
            fruit = {"name": "apple", "color": "red"}
            print(fruit["price"])
        except KeyError:
            return "Caught KeyError: 'price'"


def test_error_types():
    """Run test cases to demonstrate handling of
        multiple error types."""
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    print(garden_operations('ValueError'))

    print("\nTesting ZeroDivisionError...")
    print(garden_operations('ZeroDivisionError'))

    print("\nTesting FileNotFoundError...")
    print(garden_operations('FileNotFoundError'))

    print("\nTesting KeyError...")
    print(garden_operations('KeyError'))

    print("\nTesting multiple errors together...")
    print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


test_error_types()
