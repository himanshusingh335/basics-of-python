if __name__ == '__main__':
    print("Wrong file, run  main.py")


class Vehicle:

    def __init__(self, colour, automatic):
        self.colour = str(colour)
        self.automatic = bool(automatic)

    def changeColour(self, colour: str) -> any:
        self.colour = str(colour)


class FourWheeler(Vehicle):
    def __init__(self, colour: str, automatic: bool):
        super().__init__(colour, automatic)
        self.wheels = 4


class TwoWheeler(Vehicle):
    def __init__(self, colour: str, automatic: bool):
        super().__init__(colour, automatic)
        self.wheels = 2
