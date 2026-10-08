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
    plants = [
        Plant("Rose", 25, 30, 0.8),
        Plant("Sunflower", 80, 45, 1.2),
        Plant("Cactus", 15, 120, 0.4)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=' ')
        plant.show()
