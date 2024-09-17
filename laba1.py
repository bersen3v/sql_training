import settings as sql
from user import User, users
users : list[User] = []
print()

class Database():
    students = "Students"
    session = "Session"
    scholarship = "Scholarship"

class Column():
    number = "number"
    surname = "surname"
    name = "name"
    patronymic = "patronymic"
    sex = "sex"
    birthday = "birthday"
    group_name = "group_name"
    adress = "address"
    mark1 = "mark1"
    mark2 = "mark2"
    mark3 = "mark3"
    mark4 = "mark4"
    result = "result"
    procent = "procent"
    srbal = "srbal"
    age = "age"

sql.execute_query(f"DROP TABLE {Database.session}")
sql.execute_query(f"DROP TABLE {Database.scholarship}")
sql.execute_query(f"DROP TABLE {Database.students}")



#УПРАЖНЕНИЕ 1
#Создаем таблицу Students с ключом id
print("УПРАЖНЕНИЕ 1")
query = f"""
CREATE TABLE {Database.students} (
  {Column.number} TEXT PRIMARY KEY,
  {Column.surname} TEXT,
  {Column.name} TEXT,
  {Column.patronymic} TEXT,
  {Column.sex} TEXT,
  {Column.birthday} TEXT,
  {Column.group_name} TEXT,
  {Column.adress} TEXT
);
"""
sql.execute_query(query)
sql.show_db(Database.students)




#УПРАЖНЕНИЕ 2
#Создаем 15 записей
print("УПРАЖНЕНИЕ 2")

query = f"""
INSERT INTO
  {Database.students} ({Column.number}, {Column.surname}, {Column.name}, {Column.patronymic}, {Column.sex}, {Column.birthday}, {Column.group_name}, {Column.adress})
VALUES
"""
for user in range(15):
    user = User()
    users.append(user)
    query += user.to_string_view()+",\n"
user = User()
users.append(user)
query+=user.to_string_view()+';'
   
sql.execute_query(query)
sql.show_db(Database.students)




#УПРАЖНЕНИЕ 3
#Заменить фамилию во второй записи
# Занести в таблицу 15 записей. Для поля Группа использовать номера 156, 157 158.
# Отредактировать введенные в таблицу данные: заменить во второй записи фамилию.
# В поле Дата рождения изменить в первой записи год рождения.
# Удалить последнюю запись в таблице. Для этого нужно выделить ее: установить курсор мыши к левой границе таблицы до изменения его в виде стрелки, направленной вправо, щелкнуть мышью и нажать клавишу Delete.
# Добавить еще две записи.
print("УПРАЖНЕНИЕ 3")

query = f"""
UPDATE {Database.students}
SET {Column.surname} = 'Kirkorov'
WHERE {Column.number} = 2;
"""
sql.execute_query(query)

query = f"""
UPDATE {Database.students}
SET {Column.birthday} = '2005-03-16'
WHERE {Column.number} = 1;
"""
sql.execute_query(query)

query = f"""
DELETE FROM {Database.students}
WHERE {Column.number} = 15;
"""
sql.execute_query(query)

query = f"""
INSERT INTO
  {Database.students} ({Column.number}, {Column.surname}, {Column.name}, {Column.patronymic}, {Column.sex}, {Column.birthday}, {Column.group_name}, {Column.adress})
VALUES
"""
query += User().to_string_view()+",\n"
query+=User().to_string_view()+';'
sql.execute_query(query)

sql.show_db(Database.students)





#УПРАЖНЕНИЕ 5
#поиск по фамилии
#сортировка по фамилии
#фильтр по группе
print("УПРАЖНЕНИЕ 5")

print("поиск по фамилии")
query = f"""
SELECT * 
FROM {Database.students} 
WHERE {Column.surname} = 'Ivanov';
"""

answer = sql.execute_read_query(query)
for user in answer:
    print(user)

print('сортировка по фамилии')
query = f"""
SELECT * 
FROM {Database.students} 
ORDER BY {Column.surname};
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)

print('фильтр по группе')
query = f"""
SELECT * 
FROM {Database.students} 
WHERE {Column.group_name} = '157';
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()





#УПРАЖНЕНИЕ 6
#Осуществить поиск какого-либо студента по полю Фамилия
print("УПРАЖНЕНИЕ 6")

print("Поиск женщин")
query = f"""
SELECT * 
FROM {Database.students} 
WHERE {Column.sex} = 'female';
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()





#УПРАЖНЕНИЕ 7
#Создаем таблицу Session и Scholarship
print("УПРАЖНЕНИЕ 7")
query = f"""
CREATE TABLE {Database.session} (
  {Column.number} TEXT PRIMARY KEY,
  {Column.mark1} INTEGER,
  {Column.mark2} INTEGER,
  {Column.mark3} INTEGER,
  {Column.mark4} INTEGER,
  {Column.result} TEXT
);
"""
sql.execute_query(query)
query = f"""
CREATE TABLE {Database.scholarship} (
  {Column.result} TEXT PRIMARY KEY,
  {Column.procent} INTEGER
);
"""
sql.execute_query(query)







#УПРАЖНЕНИЕ 8
#Заполнение и связывание
print("УПРАЖНЕНИЕ 8")
query = f"""
INSERT INTO
  {Database.scholarship} ({Column.result}, {Column.procent})
VALUES
  ('Neud', 0),
  ('Ud', 100),
  ('Hor', 150),
  ('Hor1', 200),
  ('Otl', 300);
"""
sql.execute_query(query)
sql.show_db(Database.scholarship)

query = f"""
INSERT INTO
  {Database.session} ({Column.number}, {Column.mark1}, {Column.mark2}, {Column.mark3}, {Column.mark4}, {Column.result})
VALUES
"""
for user in users[:-1]:
    query+=user.for_session() + ",\n"
query+=users[-1].for_session() + ";"

sql.execute_query(query)
sql.show_db(Database.session)






#УПРАЖНЕНИЕ 10
# Подготовить список студентов, сдавших сессию на «отлично».
# Создать запрос, выводящий список студентов, имеющих хотя бы одну «тройку».
# Создать запрос, выводящий список студентов, фамилия которых начинается на букву А.
print("УПРАЖНЕНИЕ 10")

print("Поиск отличников")
query = f"""
SELECT *
FROM {Database.students}
JOIN {Database.session} ON {Database.students}.{Column.number}={Database.session}.{Column.number}
WHERE {Database.session}.{Column.result} = 'Otl'
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()

print("Поиск людей с одной тройкой")
query = f"""
SELECT *
FROM {Database.students}
JOIN {Database.session} ON {Database.students}.{Column.number}={Database.session}.{Column.number}
WHERE {Database.session}.{Column.mark2} = 3
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()

print("Поиск людей с фамилией на А")
query = f"""
SELECT *
FROM {Database.students} 
WHERE {Column.surname} LIKE 'А%'
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()






#УПРАЖНЕНИЕ 11
# Приказ
print("УПРАЖНЕНИЕ 11")
print("Сформировать приказ по процентам стипендий")
query = f"""
SELECT {Database.students}.{Column.group_name}, {Database.students}.{Column.surname}, {Database.scholarship}.{Column.procent}
FROM {Database.students}
JOIN {Database.session} ON {Database.students}.{Column.number}={Database.session}.{Column.number}
JOIN {Database.scholarship} ON {Database.scholarship}.{Column.result}={Database.session}.{Column.result}
ORDER BY {Database.students}.{Column.group_name}, {Database.students}.{Column.surname}
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()




#УПРАЖНЕНИЕ 13
# Очная Бюджетная форма
print("УПРАЖНЕНИЕ 13")
print("Вычисляемое поле среднего балла")
query = f"""
ALTER TABLE {Database.session}
ADD COLUMN {Column.srbal} real as (
  ({Column.mark1} + {Column.mark2} + {Column.mark3} + {Column.mark4})/4
);
"""
sql.execute_query(query)

query = f"""
SELECT {Database.students}.{Column.surname}, {Database.session}.{Column.srbal}
FROM {Database.students}
JOIN {Database.session} ON {Database.students}.{Column.number}={Database.session}.{Column.number}
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()




#Допы
print("Допы")
print("На отчисление")
query = f"""
SELECT {Database.students}.{Column.surname}, {Database.session}.{Column.srbal}
FROM {Database.students}
JOIN {Database.session} ON {Database.students}.{Column.number}={Database.session}.{Column.number}
WHERE {Database.session}.{Column.srbal} < 5
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()


print("Сколько лет")
query = f"""
SELECT {Column.surname}, 
    date('now')-{Column.birthday} AS {Column.age}
FROM {Database.students};
"""
answer = sql.execute_read_query(query)
for user in answer:
    print(user)
print()


print("Студенты разного пола")

for groupi in [156,157,158]:
    for sexi in ["female", "male"]:
        query = f"""
        SELECT *
        FROM {Database.students}
        WHERE {Column.group_name} = {groupi} AND {Column.sex} = "{sexi}"
        """
        answer = sql.execute_read_query(query)
        print(f'group: {groupi}, sex: {sexi}, count: {len(answer)}')
print()


