class Plant:
    class Statistics():
        def __init__(self) -> None:
            self.click_grow = 0
            self.click_age = 0
            self.click_show = 0

        def display(self) -> None:
            print(
                f"Stats: {self.click_grow} grow,{self.click_age} age "
                f"{self.click_show} show"
            )
        
    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.grow = grow
        self._stats = self.Statistics()

    def show(self) -> None:
        self._stats.click_show += 1
        print(f"{self.name}:", end=' ')
        print(f"{round(self.get_height(), 2)} cm, {self.get_age()} days old")

    def set_age(self, num: int) -> None:
        if 0 <= num:
            self._age = num
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, num: int | float) -> None:
        if 0 <= num:
            self._height = num
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int | float:
        return self._age

    def get_height(self) -> int | float:
        return self._height

    def age(self) -> None:
        self._stats.click_age += 1
        self._age += 1

    def grow(self) -> None:
        self._stats.click_grow += 1
        self._height += self.grow

    @staticmethod
    def is_more_then_year(days_old: int) -> bool:
        return days_old > 365

    @staticmethod
    def anonymus_plant() -> "Plant":
        return Plant("Unknown plant", 0, 0, 0.0)

    def show_stats(self):
        self._stats.display()


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float,
                 color: str,
                 blooming: bool) -> None:
        print("===Flower")
        super().__init__(name, height, age, grow)
        self.color = color
        self.blooming = blooming

    def bloom(self):
        if self.blooming:
            self.blooming = True
            self.show()
        else:
            print(f"[askintreeg the {self.name} to bloom]")

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree (Plant):
    class Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self.shade = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade} shade")

    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float,
                 trunk_diameter: float,
                 shade: bool,
                 ) -> None:
        super().__init__(name, height, age, grow)
        self.trunk_diameter = trunk_diameter
        self.shade = shade
        self._stats.clicks_provide_shadow = 0
        print("=== Tree")

    def produce_shade(self):
        self._stats.shade += 1
        print(f"[asking {self.name} to produce shade]")
        self.shade = True
        print(f"Tree {self.name} now produces a shade of", end=' ')
        print(f"{self.get_height()} long and {self.trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float,
                 harvest_season: str,
                 nutritional_value: int | float,
                 ) -> None:
        super().__init__(name, height, age, grow)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print("=== Vegetable")

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def nutri_boost(self) -> None:
        self.nutritional_value += 0.5

    def aged(self):
        super().age()
        self.nutri_boost()

    def growed(self):
        super().grow()
        self.nutri_boost()

class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float,
                 color: str,
                 blooming: bool) -> None:
        super().__init__(name, height, age, grow, color, blooming)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

def display_stats(plant: Plant):
    plant.show_stats()
     

if __name__ == "__main__":
    seed = Flower("Rose", 25, 30, 0.5, "red", False)
    tree = Tree("Oak", 200.0, 365, 0.1, 5.0, False)
    vegetable = Vegetable("Tomato", 5.0, 10, 1.2, "April", 0)
    anonymus = Plant.anonymus_plant()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> {Plant.is_more_then_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> {Plant.is_more_then_year(400)}"
    )
    print("=== Flower")
    seed.show()
    
    seed.bloom()
    seed.show()
    anonymus.show()
    display_stats(tree)

        