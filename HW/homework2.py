class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} is taking an action.")

    def attack(self):
        print(f"{self.name} is attacking!")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 75:
                print(f"{self.name} successfully hit the target! Arrows left: {self.arrows}")
            else:
                print(f"{self.name} missed the target. Arrows left: {self.arrows}")
        else:
            print(f"{self.name} has no arrows left!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} rested and got 5 more arrows. Arrows now: {self.arrows}")

    def status(self):
        return f"Name: {self.name}, HP: {self.hp}, Arrows: {self.arrows}, Precision: {self.precision}%"
