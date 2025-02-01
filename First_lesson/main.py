class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")
    
    def is_adult(self):
        return self.lvl >= 10


hero1 = Hero("Артем", 5, 100)
hero1.introduce()


hero2 = Hero("Богдан", 12, 150)
hero3 = Hero("Сергей", 8, 120)

print(hero1.name, "Сильный?", hero1.is_adult())
print(hero2.name, "Сильный?", hero2.is_adult())
print(hero3.name, "Сильный?", hero3.is_adult())


   