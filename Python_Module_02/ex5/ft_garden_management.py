class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception for plant-specific errors."""
    pass


class WaterError(PlantError):
    """Exception for water-related plant errors."""
    pass


class SunError(PlantError):
    """Exception for sunlight-related plant errors."""
    pass


class Plant:
    """Represents a plant with water and sunlight requirements."""
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """Manages multiple plants and handles watering and health checks."""

    def __init__(self):
        self.plants = []

    def add_plants(self, plants_data):
        """Add plants to the garden; raise error if name is empty."""

        for plant in plants_data:
            try:
                if len(plant.name) == 0:
                    raise PlantError("Error adding plant: "
                                     "Plant name cannot be empty!")
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
            except PlantError as e:
                print(e)

    def water_plants(self):
        """Water all plants and always perform cleanup."""

        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        """Check water and sunlight levels
            of all plants; raise errors if invalid."""
        for plant in self.plants:
            try:
                if plant.water < 1:
                    raise WaterError(f"Error: Water level {plant.water} "
                                     f"is too low (min 1)")
                elif plant.water > 10:
                    raise WaterError(f"Error: Water level {plant.water} "
                                     f"is too high (max 10)")
                elif plant.sun < 2:
                    raise SunError(f"Error: sun level {plant.sun} "
                                   f"is too low (min 2)")
                elif plant.sun > 12:
                    raise SunError(f"Error: sun level {plant.sun} "
                                   f"is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water}, "
                          f"sun: {plant.sun})")
            except PlantError as e:
                print(e)

    @staticmethod
    def recovery(whater_fawnd):
        """Check water availability and
            handle recovery if insufficient."""
        try:
            if whater_fawnd < 10:
                raise GardenError("Caught GardenError: Not enough water "
                                  "in tank")
            print("Enough water in the tank")
        except GardenError as e:
            print(e)
        finally:
            print("System recovered and continuing...")


def test_garden_management():
    """Run test cases for adding, watering, and checking plant health."""
    p1 = Plant("tomato", 5, 8)
    p2 = Plant("lettuce", 15, 8)
    p3 = Plant("", 5, 15)
    p4 = Plant("botato", 4, 10)

    plants_data = [p1, p2, p3, p4]
    garden = GardenManager()
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    garden.add_plants(plants_data)

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    garden.check_plant_health()

    print("\nTesting error recovery...")
    garden.recovery(9)

    print("\nGarden management system test complete")


test_garden_management()
