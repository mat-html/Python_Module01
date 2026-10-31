class Plant:
    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float) -> None:
        self.name = name
        self._height = height
        self._days_old = days_old
        self.growing = growing

    def show(self) -> None:
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
        self._days_old += 1

    def grow(self) -> None:
        self._height += self.growing


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float,
                 color: str,
                 blooming: bool) -> None:
        print("===Flower")
        super().__init__(name, height, days_old, growing)
        self.color = color
        self.blooming = blooming

    def bloom(self):
        if self.blooming:
            self.blooming = True
            self.show()
        else:
            print(f"[asking the {self.name} to bloom]")

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree (Plant):
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
        print("=== Tree")

    def produce_shade(self):
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
        print("=== Vegetable")

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def nutri_boost(self) -> None:
        self.nutritional_value += 0.5

    def age(self):
        super().age()
        self.nutri_boost()

    def grow(self):
        super().grow()
        self.nutri_boost()


if __name__ == "__main__":
    p1 = Flower("Rose", 25, 30, 0.5, "red", False)
    p1.show()
    p1.bloom()

    p2 = Tree("Oak", 200.0, 365, 0.1, 5.0, False)
    p2.show()
    p2.produce_shade()

    i = 0
    p3 = Vegetable("Tomato", 5.0, 10, 1.2, "April", 0)
    p3.show()
    print("[make tomato grow and age]")
    for i in range(i, 20):
        p3.grow()
        p3.age()
    p3.show()
