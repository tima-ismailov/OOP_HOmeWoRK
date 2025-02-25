# #Множественное Наследование (родительские классы)

# #Горизантальный наследование 
# class Flyeble:

#     def fly(self):
#         return "Летит"
    
# class Swimmable:

#     def swim(self):
#         return "Плавает"
    
# class Duck(Flyeble, Swimmable):

#     def make_sound(self):
#         return "Кря-Кря"
    

# donald_duck = Duck ()
# print(donald_duck.fly())
# print(donald_duck.swim())


#Ромбовидное наследование 

# class Animal:
    
#     def make_sound(self):
#         return "Издает звук"
    
#     def action(self):
#         return "Базовое действие"
    
# class Flyeble(Animal):

#     def action(self):
#         return "Летит"
    
# class Swimmable(Animal):

#     def action(self):
#         return "Плавает"
    

# class Duck(Flyeble, Swimmable):

#     def make_sound(self):
#         return "Кря-Кря"
#     def action(self):
#         return "Летает и плавает "

# donald_duck = Duck ()
# print(donald_duck.action())


import sqlite3

#Создание таблицы и имя
connect =  sqlite3.connect("User.db")

#Переменная которая поможет нам писать 
cursor = connect.cursor()

#Создание базы данных
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INT NOT NULL,
        hobby  TEXT
   )
                ''')



#Сохранение = Изменение 
connect.commit()

def add_user(name, age, hobby):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

# add_user("John", 33, "Swimming")


def get_all_users():

    cursor.execute('SELECT * FROM users ')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    
get_all_users()