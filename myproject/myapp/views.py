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
        
        return HttpResponse(f'Имя: {name}, Email: {email}')

    else:
        # Отображение пустой формы
        return render(request, 'myapp/form.html')