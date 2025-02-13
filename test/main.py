# class Hero:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp

#     def intoduce(self):
#         return f"Привет,меня зовут {self.name} мой уровень {self.lvl}   мое hp {self.hp}"

#     def is_adult(self):
#         if self.lvl >= 10:
#             return True
#         else:
#             return False


# superman = Hero("Klark Kent", 15, 150)
# print(superman.intoduce())


# ironman = Hero("Tony Stark", 9, 120)
# halk = Hero("halk", 20, 250)
# print(ironman.is_adult())
# print(halk.is_adult())
import random

class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        self.hp += 100
        return f"HP plus 100"
    
    def attack(self):
        return f"{self.name} attacks someone"
    
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows < 1:
            return "Увас нет стрел"
        self.arrows -= 1
        if random.randint(1, 100) < self.precision:
            return f"{self.name}   попал в цель"
        else:
            return f"{self.name} не попал"
        
    def rest(self):
        self.arrows += 5
        return f"Количество стрел увеличилось до {self.arrows}"
    
    def status(self):
        return f"Имя: {self.name}\n Здоровье: {self.hp}\n Стрелы: {self.arrows}\n Точность: {self.precision}"
    

Archer1 = Archer("Tima", 250, 15, 72)
print(Archer1.attack())
print(Archer1.rest())
print(Archer1.status())

