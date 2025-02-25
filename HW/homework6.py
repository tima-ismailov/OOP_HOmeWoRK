
import sqlite3

connect =  sqlite3.connect("User.db")

cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INT NOT NULL,
        hobby  TEXT
   )
                ''')




connect.commit()

# def add_user(name, age, hobby):

#     cursor.execute(
#         'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
#         (name, age, hobby)
#     )
#     connect.commit()
#     print(f"Пользователь {name} добавлен")

# # add_user("John", 33, "Swimming")


# def get_all_users():

#     cursor.execute('SELECT * FROM users ')
#     users = cursor.fetchall()
#     print(users)
#     print('Список всех пользователей')

#     for i in users:
#         print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    
# get_all_users()

def get_user():
    name = input("enter name: ")

    cursor.execute('SELECT * FROM users WHERE name = ?', (name, ))
    user = cursor.fetchall()

    if user:
        print('User not found:')
        for u in user:
            print(f'name: {u[0]}, age; {u[1]}, hobby: {u[2]}')
    else:
        print(f'No user found with name {name}')

    
get_user("")