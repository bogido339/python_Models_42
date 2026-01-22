class Plant:
    """Represents a basic plant"""

    def __init__(self, name, height):
        """Create a plant with name and height"""
        self.name = name
        self.height = height

    def grow(self, x: int):
        """Increase plant height by x"""
        self.height += x

    def get_info(self):
        """Return plant information"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Represents a plant that has flowers"""

    def __init__(self, name, height, f_color):
        """Create a flowering plant with color"""
        super().__init__(name, height)
        self.f_color = f_color

    def flowering(self):
        """Return flowering status"""
        return "blooming"

    def get_info(self):
        """Return flowering plant information"""
        return (f"{self.name}: {self.height}cm, "
                f"{self.f_color} flowers ({self.flowering()})")


class PrizeFlower(FloweringPlant):
    """Represents a flowering plant with prize points"""

    def __init__(self, name, hight, f_color, p_point):
        """Create a prize flower with points"""
        super().__init__(name, hight, f_color)
        self.p_point = p_point

    def flowering(self):
        """Return flowering status"""
        return "blooming"

    def get_info(self):
        """Return prize flower information"""
        return (f"{self.name}: {self.height}cm, "
                f"{self.f_color} flowers ({self.flowering()}). "
                f"Prize points: {self.p_point}")


class GardenManager:
    """Manages multiple gardens"""

    gardens = []

    class Garden:
        """Represents a single garden"""

        def __init__(self, owner):
            """Create a garden for one owner"""
            self.owner = owner
            self.plants = []
            self.total_growth = 0

        def add_plant(self, plant):
            """Add a plant to the garden"""
            self.plants.append(plant)
            return f"Added {plant.name} to {self.owner}'s garden"

        def grow_all(self):
            """Grow all plants by 1cm"""
            v = 1
            for plant in self.plants:
                plant.grow(v)
                self.total_growth += v
                print(f"{plant.name} grew {v}cm")

        def get_info(self):
            """Print information of all plants"""
            for plant in self.plants:
                print(plant.get_info())

        def garden_score(self):
            """Calculate garden score"""
            score = 0
            for plant in self.plants:
                score += plant.height + 10
                if isinstance(plant, PrizeFlower):
                    score += plant.p_point
            return score

    @classmethod
    def add_garden(cls, garden):
        """Add a garden to the manager"""
        cls.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        """Return number of gardens"""
        return len(cls.gardens)

    class GardenStats:
        """Provides statistics for a garden"""

        def __init__(self, garden):
            """Create stats object for a garden"""
            self.garden = garden

        def count_plants(self):
            """Return number of plants"""
            return len(self.garden.plants)

        def plant_types(self):
            """Count plant types"""
            regular = flowering = prize = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def total_growth(self):
            """Return total growth"""
            return self.garden.total_growth

        def height_validatio(self):
            """Check if all plant heights are valid"""
            for plant in self.garden.plants:
                if plant.height < 0:
                    return False
            return True


oak = Plant('Oak Tree', 100)
rose = FloweringPlant('Rose', 25, 'red')
sun = PrizeFlower('Sunflower', 50, 'yellow', 10)

flawer = Plant('Flawer', 82)

manager = GardenManager
garden = GardenManager.Garden
alice = garden('Alice')
bob = garden('Bob')

print("=== Garden Management System Demo ===\n")
print(alice.add_plant(oak))
print(alice.add_plant(rose))
print(alice.add_plant(sun))
bob.add_plant(flawer)

print("")
print(f"{alice.owner} is helping all plants grow...")
alice.grow_all()

print("")
print("=== Alice's Garden Report ===")
print("Plants in garden:")
alice.get_info()

stat = GardenManager.GardenStats(alice)
regular, flowering, prize = stat.plant_types()

print("")
print(f"Plants added: {stat.count_plants()}, "
      f"Total growth: {stat.total_growth()}cm")
print(f"Plant types: {regular} regular, "
      f"{flowering} flowering, {prize} prize flowers")

print("")
manager.add_garden(alice)
manager.add_garden(bob)

print(f"Height validation test: {stat.height_validatio()}")
print(f"Garden scores - Alice: {alice.garden_score()}, "
      f"Bob: {bob.garden_score()}")
print(f"Total gardens managed: {manager.create_garden_network()}")
