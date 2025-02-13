def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__} с аргументами {args}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello {name}")

greet("Alica")

class Rectangle:
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height

    def __str__(self):
        return f"Прямоугольник {self.wight}x{self.height}"
    
    def __add__(self, other):
        return Rectangle(self.wight + other.wight, self.height + other.height)
    
rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(2, 5)
rectangle3 = rectangle1 + rectangle2

print(rectangle1)
print(rectangle2)
print(rectangle3)
        