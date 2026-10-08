class Plant:
    def __init__(self,
                 name: str,
                 height: int | float,
                 age: int,
                 grow: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.grow = grow
        print(f"Plant created: {self.name}:", end=' ')
        print(f"{self.get_height()} cm, {self.get_age()} days old")

    def show(self) -> None:
        print(f"Current state: {self.name}:", end=' ')
        print(f"{self.get_height()} cm, {self.get_age()} days old")

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


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30, 0.8)
    plant.set_height(30)
    plant.set_height(-50)
    plant.set_age(-5)
    plant.show()
