class PlantNameError(Exception):
    """Exception for invalid plant names."""
    pass


def water_plants(plant_list):
    """Water each plant; catch invalid plant names
        and ensure cleanup."""
    is_completed = True
    try:
        for plant in plant_list:
            try:
                if not isinstance(plant, str):
                    raise PlantNameError("Error: Cannot water None - "
                                         "invalid plant!")
                else:
                    print(f"Watering {plant}")
            except PlantNameError as e:
                is_completed = False
                print(e)
    finally:
        print("Closing watering system (cleanup)")

    if is_completed:
        print("Watering completed successfully!")


def test_watering_system():
    """Run test cases to demonstrate watering system with good
        and bad plants."""
    good_plant_list = ["tomato", "lettuce", "carrots"]
    bad_plant_list = ["tomato", 10, "carrots"]

    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plants(good_plant_list)

    print("\nTesting with error...")
    water_plants(bad_plant_list)

    print("\nCleanup always happens, even with errors!")


test_watering_system()
