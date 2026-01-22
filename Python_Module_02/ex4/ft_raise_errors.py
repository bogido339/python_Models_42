def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if plant name, water level, and sunlight hours are valid;
        raise errors if not."""
    try:
        if len(plant_name) == 0:
            raise ValueError("Error: Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too low (min 1)")

        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(e)


def test_plant_checks():
    """Run test cases to verify plant health checks
        with valid and invalid values."""

    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("rose", 5, 11)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 11)

    print("\nTesting bad water level...")
    check_plant_health("rose", 15, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("rose", 0, 5)

    print("\nAll error raising tests completed")


test_plant_checks()
