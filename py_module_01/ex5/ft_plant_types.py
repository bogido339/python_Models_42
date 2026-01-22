class Plant:
    """Represents a basic plant"""

    def __init__(self, name, height, age):
        """Create a plant with name, height, and age"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flowering plant"""

    def __init__(self, name, height, age, color):
        """Create a flower with color"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Show flower blooming"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a tree"""

    def __init__(self, name, height, age, area):
        """Create a tree with shade area"""
        super().__init__(name, height, age)
        self.area = area

    def produce_shade(self, n):
        """Show produced shade size"""
        print(f"{self.name} provides {n} square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable plant"""

    def __init__(self, name, height, age, harvest):
        """Create a vegetable with harvest season"""
        super().__init__(name, height, age)
        self.harvest = harvest

    def nutrition(self, n):
        """Show nutrition value"""
        print(f"{self.name} is rich in {n}")


F1 = Flower("Rosa", 25, 30, "red")
F2 = Flower("bosa", 20, 33, "bleu")

T1 = Tree("Oak", 500, 1825, 50)
T2 = Tree("bak", 623, 2000, 80)

V1 = Vegetable("Tomato", 80, 90, "summer")
V2 = Vegetable("Botato", 90, 50, "winter")

print("=== Garden Plant Types ===")
print("")
print(f"{F1.name} ({type(F1).__name__}): "
      f"{F1.height}cm, {F1.age} days, {F1.color} color")
print(f"{F2.name} ({type(F2).__name__}): "
      f"{F2.height}cm, {F2.age} days, {F2.color} color")
F1.bloom()
F2.bloom()
print("")
print(f"{T1.name} ({type(T1).__name__}): "
      f"{T1.height}cm, {T1.age} days, {T1.area}cm diameter")
print(f"{T2.name} ({type(T2).__name__}): "
      f"{T2.height}cm, {T2.age} days, {T2.area}cm diameter")
T1.produce_shade(78)
T2.produce_shade(87)
print("")
print(f"{V1.name} ({type(V1).__name__}): "
      f"{V1.height}cm, {V1.age} days, {V1.harvest} harvest")
print(f"{V2.name} ({type(V2).__name__}): "
      f"{V2.height}cm, {V2.age} days, {V2.harvest} harvest")
V1.nutrition("vitamin C")
V2.nutrition("vitamin A")
