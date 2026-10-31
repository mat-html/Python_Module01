class Plant:
    class Statistics():
        def __init__(self) -> None:
            self.click_grow = 0
            self.click_age = 0
            self.click_show = 0

        def display(self) -> None:
            print(
                f"Stats: {self.click_grow} grow, {self.click_age} age, "
                f"{self.click_show} show"
            )

    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float | int) -> None:
        self.name = name
        self._height = height
        self._days_old = days_old
        self.growing = growing
        self._stats = self.Statistics()

    def show(self) -> None:
        self._stats.click_show += 1
        print(f"{self.name}:", end=' ')
        print(f"{round(self.get_height(), 2)} cm, {self.get_age()} days old")

    def set_age(self, num: int) -> None:
        if 0 <= num:
            self._days_old = num
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
        return self._days_old

    def get_height(self) -> int | float:
        return self._height

    def age(self) -> None:
        self._stats.click_age += 1
        self._days_old += 1

    def grow(self) -> None:
        self._stats.click_grow += 1
        self._height += self.growing

    @staticmethod
    def is_more_then_year(year_old: int) -> bool:
        return year_old > 365

    @staticmethod
    def anonymus_plant() -> "Plant":
        return Plant("Unknown plant", 0, 0, 0.0)

    def show_stats(self):
        self._stats.display()


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float,
                 color: str,
                 blooming: bool) -> None:
        super().__init__(name, height, days_old, growing)
        self.color = color
        self.blooming = blooming

    def bloom(self):
        self.blooming = True
        self.show()

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
            self.clicks_provide_shadow = 0

        def display(self) -> None:
            super().display()
            print(f"{self.clicks_provide_shadow} shade")

    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float,
                 trunk_diameter: float,
                 shade: bool,
                 ) -> None:
        super().__init__(name, height, days_old, growing)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self):
        self._stats.clicks_provide_shadow += 1
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
                 days_old: int,
                 growing: float,
                 harvest_season: str,
                 nutritional_value: int | float,
                 ) -> None:
        super().__init__(name, height, days_old, growing)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def nutri_boost(self) -> None:
        self.nutritional_value += 0.5

    def agese(self):
        super().age()
        self.nutri_boost()

    def growed(self):
        super().grow()
        self.nutri_boost()


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float,
                 color: str,
                 blooming: bool) -> None:
        super().__init__(name, height, days_old, growing, color, blooming)
        self.seeds = 0

    def bloom(self):
        self.seeds = 42
        super().bloom()

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant):
    plant.show_stats()


if __name__ == "__main__":
    flower = Flower("Rose", 25, 30, 0.5, "red", False)
    tree = Tree("Oak", 200.0, 365, 0.1, 5.0, False)
    seed = Seed("Tomato", 5.0, 10, 1.2, "Red", False)
    anonymus = Plant.anonymus_plant()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> {Plant.is_more_then_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> {Plant.is_more_then_year(400)}"
    )

    print("\n=== Flower")
    flower.show()
    print("[statistics for Rose]")
    display_stats(flower)
    print("[asking Rose to grow and bloom]")
    flower.grow()
    flower.bloom()
    print("[statistics for Rose]")
    display_stats(flower)
    print("\n")

    print("=== Tree")
    tree.show()
    print("[statistics for Oak]")
    display_stats(tree)
    tree.produce_shade()
    print("[statistics for Oak]")
    display_stats(tree)
    print("\n")

    print("=== Seed")
    seed.show()
    print("[make tomato grow, age and bloom]")
    seed.age()
    seed.grow()
    seed.bloom()
    print("[statistics for Tomato]")
    display_stats(seed)
    print("\n")

    print("=== Anonymus")
    anonymus.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymus)
