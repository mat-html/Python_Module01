class Plant:
    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old
        self.growing = growing

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)} cm, "
              f"{self.days_old} days old")

    def age(self) -> None:
        self.days_old += 1

    def grow(self) -> None:
        self.height += self.growing


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
