def check_temperature(temp_str):
    """Check if input is a valid temperature and within 0-40°C for plants."""
    try:
        int(temp_str)

        if temp_str < 0:
            return f"Error: {temp_str}°C is too cold for plants (min 0°C)"
        elif temp_str > 40:
            return f"Error: {temp_str}°C is too hot for plants (max 40°C)"
        else:
            return f"Temperature {temp_str}°C is perfect for plants!"

    except ValueError:
        return f"Error: {temp_str} is not a valid number"


def test_temperature_input():
    """Run test cases to verify check_temperature function works correctly."""
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    print(check_temperature(25))
    print("\nTesting temperature: 'abc'")
    print(check_temperature('abc'))
    print("\nTesting temperature: 100")
    print(check_temperature(100))
    print("\nTesting temperature: -50")
    print(check_temperature(-50))
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
