class Plant:
    def __init__(self,
                 name: str,
                 height: int | float,
                 days_old: int,
                 growing: float = 0.3) -> None:
        self.name = name
        if height < 0:
            self._height = 0.0
        else:
            self._height = height
        if days_old < 0:
            self._days_old = 0
        else:
            self._days_old = days_old
        self._days_old = days_old
        self.growing = growing
        print(f"Plant created: {self.name}:", end=' ')
        print(f"{self.get_height()} cm, {self.get_age()} days old")

    def show(self) -> None:
        print(f"Current state: {self.name}:", end=' ')
        print(f"{self.get_height()} cm, {self.get_age()} days old")

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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10, 0.8)
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-50)
    plant.set_age(-5)
    print()
    plant.show()
