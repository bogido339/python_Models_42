class Plant:
    """Represents a plant with protected height and age"""

    def __init__(self, name, height, age):
        """Create a plant and validate height and age"""
        self.name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        """Set plant height if value is valid"""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        """Set plant age if value is valid"""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        """Return plant height"""
        return self._height

    def get_age(self):
        """Return plant age"""
        return self._age


print("=== Garden Security System ===")
print("Plant created: Rose")
plant1 = Plant("Rosa", 25, 30)
print("")
plant1.set_height(-5)
print("")

print(f"Current plant: {plant1.name} ({plant1.get_height()}cm, "
      f"{plant1.get_age()} days)")
