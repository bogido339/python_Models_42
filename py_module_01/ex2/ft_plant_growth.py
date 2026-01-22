class Plant:
    """Represents a plant with growth and age"""

    def __init__(self, name, height, age):
        """Create a plant with initial data"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase height by 1cm"""
        self.height += 1

    def extra_age(self):
        """Increase age by 1 day"""
        self.age += 1

    def get_info(self):
        """Print plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


p1 = Plant("Rose", 25, 30)

print("=== Day 1 ===")
p1.get_info()

for i in range(6):
    p1.grow()
    p1.extra_age()

print("=== Day 7 ===")
p1.get_info()
print(f"Growth this week: +{i + 1}cm")
