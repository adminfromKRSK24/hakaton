# from django.shortcuts import render

# def my_view(request):
#     # Данные для передачи в шаблон
#     context = {
#         'title': 'Моя страница',
#         'header': 'Привет, !',
#         'content': 'Это динамический контент страницы.'
#     }
#     # Рендеринг шаблона с данными
#     return render(request, 'myapp/my_template.html', context)

# from django.shortcuts import render
# from django.http import HttpResponse

# def my_view(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         # Вывод данных (например, сохранение в БД или просто ответ пользователю)
#         return HttpResponse(f'Имя: {name}, Email: {email}')
#     else:
#         # Отображение пустой формы
#         return render(request, 'myapp/form.html')


# # Create your views here.

from django.shortcuts import render, HttpResponse
from .data_store import TempUserData
from myapp.models import Users
import sqlite3

import sqlite3

def add_user(database: str, user: list[str]):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    # Используем параметризованный запрос для избежания SQL-инъекций
    query = "INSERT INTO users (Surname, Name, Phone, Email) VALUES (?, ?, ?, ?);"
    
    try:
        cursor.execute(query, (user[0], user[1], user[2], user[3]))
        print(f"Пользователь {user[1]} добавлен.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка добавления пользователя: {e}")
    
    connection.commit()
    connection.close()


# def add_user(database: str, user: list[str]):
#     connection = sqlite3.connect(database)
#     cursor = connection.cursor()

#     query = f"insert into users (Surname, Name, Phone, Email) values ('{user[0]}', '{user[1]}', '{user[2]}', '[{user[3]}]');"
#     # query = f"insert into users (Name, Email) values ('{user[0]}', '{user[1]}', '{user[2]}', '[{user[3]}]');"
#     cursor.execute(query)
    
#     # Добавить нового пользователя в существующую таблицу
#     # new_user = Users(name='Петр Петров', email='petr@example.com')
#     # new_user.save()

#     connection.commit()
#     connection.close()

# def my_view(request):
#     if request.method == 'POST':
#         # Получаем данные напрямую из HTML-формы через request.POST
#         name = request.POST.get('name')
#         email = request.POST.get('email')
        
#         # name = request.POST.get('name')
#         # surname = request.POST.get('surname')
#         # phone = request.POST.get('phone')
#         # email = request.POST.get('email')

#         if name and email:  # Проверяем, что поля заполнены
#             # Сохраняем данные во временный класс
#             temp_user = TempUserData(name=name, email=email)
#             print(temp_user)
            
            
#             # database = '../myproject/DB1.db'
#             # user = ['Иванов', 'Иван', '8-953-000-00-01', 'abc@mail.ru']
#             # user = ['Иван', 'abc@mail.ru']
            
#             # add_user(database, user)
#             # Передаем данные из класса в базу данных
#             saved_user = temp_user.save_to_database()
#             # saved_user = temp_user.add_user(database, user)

#             return HttpResponse(f'Данные сохранены в базе: Имя - {saved_user.name}, Email - {saved_user.email}')
#         else:
#             return HttpResponse('Ошибка: поля должны быть заполнены')
#     else:
#         return render(request, 'myapp/form.html')

# просто страница

# def my_view(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         # Вывод данных (например, сохранение в БД или просто ответ пользователю)
#         return HttpResponse(f'Имя: {name}, Email: {email}')
#     else:
#         # Отображение пустой формы
#         return render(request, 'myapp/form.html')

# def add_user(database: str, user: list[str]):
#     connection = sqlite3.connect(database)
#     cursor = connection.cursor()

#     query = f"insert into users (Surname, Second_name, Phone, Email) values ('{user[0]}', '{user[1]}', '{user[2]}', '[{user[3]}]');"
#     cursor.execute(query)

#     connection.commit()
#     connection.close()
    
def my_view(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        database = 'DB1.db'
        user_data = [surname, name, phone, email]

        add_user(database, user_data)

        
        # Получить все записи
        # users = Users.objects.all()

                # # Вывести всех пользователей
                # for user in users:
                #     print(user.name, user.email)

        # Добавить нового пользователя в существующую таблицу
        # new_user = Users(Surname="hgfhdf", Name, Phone="+789789678678", Email)
        # new_user.save()

        # Обновить данные пользователя
        # user = Users.objects.get(id=1)
        # user.name = 'Иван Иванов'
        # user.save()
        

        # Вывод данных (например, сохранение в БД или просто ответ пользователю)
        # list_user = ["Gtnhjd", name, "+78778978978", email]
        # print(list_user)
        
        # add_user("../myproject/DB1.db", list_user)
        
        # new_user = Users(name='Петр Петров', email='petr@example.com')
        # new_user.save()
        return HttpResponse(f'Имя: {name}, Email: {email}')

    else:
        # Отображение пустой формы
        return render(request, 'myapp/form.html')