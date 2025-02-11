#Декораторы
 
def my_decorator(func):
    
    def wrapper():
        print("Перед выполнением функции")
        func()
        print("После выполнения функции")

    return wrapper


@my_decorator
def hello():
    print("привет мир")


# hello()


#Декораторы с аргументами
         #n = 3
def repeat(n): # step 2
         #func = greet()
    def decorator(func): # step 3
         
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
            
        return wrapper
    return decorator



@repeat(3)
def greet():
    print("Привет!!")

# greet()  # вызов фунции     


# Декоратор для класса 
   #в cls хрониться myclass используется наследственость
def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print("Новый метод")
        
    return NewClass

@class_decorator
class MyClass:
    def old_method(self):
        return print("Старый медот")
    

# obj = MyClass() #NewClass()
# obj.old_method()
# obj.new_method()



class Person:
    #Конструктор | Магическйи метод
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self,):
        return f"бла бла бла"
    

# obj =  Person("Tilek", 76)

# print(obj)


class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __str__(self):
        return f"{self.amount} СОМ"
        
m1 = Money(100)
m2 = Money(100)
m3 = m1 + m2
# print(m3)


class Math:

    @staticmethod
    def add(self, a, b):
        return a + b 
    
obj3 = Math()

print(obj3.add(1,2)) 