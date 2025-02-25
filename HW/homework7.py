import sqlite3

connect = sqlite3.connect('User.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject VARCHAR (50) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
               ''')

connect.commit()

def add_grade(user_id, subject, grade):
    cursor.execute('''
            INSERT INTO grades (user_id, subject, grade) VALUES (?,?,?)
                   ''',
                   (user_id, subject, grade))
    connect.commit()
    print(f"Оценка добавлена для пользователя с ID {user_id}!!!")

def update_grade(grade_id, new_grade):
    cursor.execute('''
        UPDATE grades 
        SET grade = ? 
        WHERE grade_id = ?
    ''', (new_grade, grade_id))
    
    connect.commit()
    print(f"Grade for subject with ID {grade_id} updated!")

add_grade(1, "Математика", 5)
add_grade(2, "Русский", 4)
update_grade(1, 4)

def get_users_with_grades():
    cursor.execute('''
        SELECT users.name, users.age, grades.subject, grades.grade
        FROM users 
        LEFT JOIN grades ON users.user_id = grades.user_id
                   ''')
    
    users = cursor.fetchall()
    for i in users:
        print(f"NAME: {i[0]}, SUBJECT: {i[2]}, GRADE: {i[3]}")

get_users_with_grades()