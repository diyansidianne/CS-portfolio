class Glassware:
    def __init__(self, material="Glass"):
        self.material = material

    def describe(self):
        return f"This glassware is made of {self.material}."


class Beaker(Glassware):
    def __init__(self, capacity_ml):
        super().__init__()
        self.capacity_ml = capacity_ml

    def describe(self):
        return f"Beaker with a capacity of {self.capacity_ml} mL."


class Tray:
    def __init__(self):
        self.beakers = [Beaker(250) for _ in range(5)]

    def show_inventory(self):
        for i, beaker in enumerate(self.beakers, start=1):
            print(f"Beaker {i}: {beaker.describe()}")


tray = Tray()
tray.show_inventory()

del tray