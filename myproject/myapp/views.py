from django.shortcuts import render, HttpResponse
from .data_store import TempUserData
from myapp.models import Users
import sqlite3
from django.http import JsonResponse


def add_event(database: str, event: list[str]):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    query = "insert into Event (date, time_start, time_end, Name, Place, Interes, Spiker) values (?, ?, ?, ?, ?, ?, ?);"

    try:
        cursor.execute(query, (event[0], event[1], event[2], event[3], event[4], event[5], event[6]))
        print(f"Событие добавлено.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка добавления события: {e}")

    connection.commit()
    connection.close()

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
 
def index(request):
    return render(request, 'myapp/home.html')   
    
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
        return render(request, 'myapp/register.html')
        
# Функция для обработки формы создания мероприятия
def get_post_event(request):
    if request.method == 'POST':
        
        # Получение данных из формы
        event_type = request.POST.get('type')  # Тип события
        theme = request.POST.get('theme')  # Тема мероприятия
        tags = request.POST.getlist('tags[]')  # Интересы (теги), несколько значений
        city = request.POST.get('city')  # Город
        location = request.POST.get('location')  # Место проведения
        date = request.POST.get('date')  # Дата мероприятия
        start_time = request.POST.get('start-time')  # Время начала
        end_time = request.POST.get('end-time')  # Время окончания
        min_participants = request.POST.get('min-participants')  # Минимальное количество участников
        max_participants = request.POST.get('max-participants')  # Максимальное количество участников

        database = 'DB1.db'

        event_data = [date, start_time, end_time, city, location, theme, event_type]

        add_event(database, event_data)
        
        return HttpResponse(f'Имя: {event_data[0]}, Email: {event_data[1]}')

    else:
        # Если метод запроса не POST, отображаем пустую форму
        return render(request, 'myapp/event.html')