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
        print(
            f"{self.name}: {round(self.height, 2)} cm, "
            f"{self.days_old} days old"
            )

    def age(self) -> None:
        self.days_old += 1

    def grow(self) -> None:
        self.height += self.growing


if __name__ == "__main__":
    i = 0
    p1 = Plant("Rose", 25, 30, 0.8)
    p2 = Plant("Sunflower", 80, 45, 1.2)
    p3 = Plant("Cactus", 15, 120, 0.4)
    print("=== Garden Plant Growth ===")
    p3.show()

    for i in range(i, 7):
        print(f"=== Day {i + 1} ===")
        p3.age()
        p3.grow()
        p3.show()
