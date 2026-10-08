class Plant:
    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.grow = grow

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)} cm, {self.age} days old")

    def aged(self) -> None:
        self.age += 1

    def growed(self) -> None:
        self.height += self.grow


if __name__ == "__main__":
    i = 0
    p1 = Plant("Rose", 25, 30, 0.8)
    p2 = Plant("Sunflower", 80, 45, 1.2)
    p3 = Plant("Cactus", 15, 120, 0.4)
    print("=== Garden Plant Growth ===")
    p3.show()

    for i in range(i, 7):
        print(f"=== Day {i + 1} ===")
        p3.aged()
        p3.growed()
        p3.show()
