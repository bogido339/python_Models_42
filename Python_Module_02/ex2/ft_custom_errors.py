class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception for plant-specific errors."""
    pass


class WaterError(PlantError):
    """Exception for water-related errors in plants."""
    pass


def check_plant_health(status):
    """Raise PlantError if the plant is wilting."""
    if status == "wilting":
        raise PlantError("The tomato plant is wilting!")


def check_water_level(level):
    """Raise WaterError if water level is below 10."""
    if level < 10:
        raise WaterError("Not enough water in the tank!")


def test_garden_error():
    """Run test cases to demonstrate custom garden errors."""
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant_health("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_level(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    cases = {
        lambda: check_plant_health("wilting"),
        lambda: check_water_level(5)
    }
    for func in cases:
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


test_garden_error()
