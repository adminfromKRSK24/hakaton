from django.shortcuts import render, HttpResponse
from .data_store import TempUserData
from myapp.models import Users
import sqlite3
from django.http import JsonResponse
from bs4 import BeautifulSoup
from myapp.events import *
from myapp.mail import *

# import os
# from django.conf import settings

# def get_event(database: str):
#     connection = sqlite3.connect(database)
#     cursor = connection.cursor()
    
#     query = f'SELECT * FROM Events ORDER BY id DESC LIMIT 1'
#     cursor.execute(query)
#     events = cursor.fetchone()

#     connection.close()

#     return list(events) if events else []


# def add_event_for_calendar(html_page: str, event: list[str]):
#     date = event[1]
#     start_time = event[2]
#     end_time = event[3]
#     name_event = event[4]
#     city = event[5]
#     tags = event[6]
#     location = event[9]

#     with open(html_page, 'r', encoding='utf-8') as file:
#         html_content = file.read()
#     soup = BeautifulSoup(html_content, 'html.parser')

#     old_tag = soup.body
#     new_tag = soup.new_tag("div", class_="event")
#     event_html = f"""
#         <b><h3>{date}</h3></b>
#         <p>Мероприятие {name_event} будет проходить в городе {city}</p>
#         <p>Место проведения: {location}</p>
#         <p>Начало мероприятия: {start_time}</p>
#         <p>Конец мероприятия: {end_time}</p>
#         <p>Интересы: {tags}</p>
#         <hr/>
#     """
#     parced_html = BeautifulSoup(event_html, 'html.parser')
#     new_tag.append(parced_html)
#     old_tag.insert(-2, new_tag)
#     with open(html_page, 'w', encoding='utf-8') as file:
#         file.write(str(soup))

def add_event(database: str, event: list[str]):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    query = "insert into Events (date, time_start, time_end, Name, City, Interes, Spiker, Categoris, Place) values (?, ?, ?, ?, ?, ?, ?, ?, ?);"

    try:
        cursor.execute(query, (event[0], event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8]))
        print(f"Событие добавлено.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка добавления события: {e}")

    connection.commit()    
    connection.close()
    
    event = get_event(database)
    page = "./myapp/templates/myapp/calendar.html"
    add_event_for_calendar(page, event)
    
def get_list_interes(all_interests, my_interests):
    common_elements = set(all_interests).intersection(my_interests)
    
    return common_elements

def add_id_user_in_table(database: str, event: list[str], id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    all_interests = ["IT", "Sport", "Business", "Auto"]
    
    list_interes = get_list_interes(all_interests, event)
    
    for i in list_interes:
        query = f"INSERT INTO {i} (id_user) VALUES (?);"
        try:
            cursor.execute(query, (id,))  # Передаем id как кортеж
            print(f"Событие добавлено.")
        except sqlite3.IntegrityError as e:
            print(f"Ошибка добавления события: {e}")

    connection.commit()    
    connection.close()

def get_user_id(database: str):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    # Используем параметризованный запрос для избежания SQL-инъекций
    query = f'select max(id) from "Users";'
    try:
        cursor.execute(query)
        temp = cursor.fetchone()
        user_id = temp[0]
        print(f"id найден.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка id {e}")
    
    connection.close()
    
    return user_id

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

def show_calendar(request):
    return render(request, 'myapp/calendar.html')  
    
def my_view(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        tags = request.POST.getlist('tags[]')  # Интересы (теги), несколько значений
        
        body = "Спасибо за регистрацию!"
        subject = "Регистрация"
        email_list = []
        email_list.append(email)
        
        database = 'DB1.db'
        user_data = [surname, name, phone, email]

        add_user(database, user_data)
        user_id = get_user_id(database)
        add_id_user_in_table(database, tags, user_id)
        
        sending_letters(email_list, body, subject)
        
        
        return HttpResponse(f'Имя: {name}, Email: {email}')

    else:
        # Отображение пустой формы
        return render(request, 'myapp/register.html')
        


def get_email_list(database: str, tag: str):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    # Используем параметризованный запрос для избежания SQL-инъекций
    query = f'select Email from Users join {tag} on Users.id = {tag}.id_user;'
    
    try:
        cursor.execute(query)
        temp = cursor.fetchall()
        email_list = [elem[0] for elem in temp]
        print(f"tag найден")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка tag {e}")
    
    connection.close()
    
    return email_list

# Функция для обработки формы создания мероприятия
def get_post_event(request):
    if request.method == 'POST':
        
        # Получение данных из формы
        event_type = request.POST.get('type')  # Тип события
        theme = request.POST.get('theme')  # Тема мероприятия
        # tags = request.POST.getlist('tags')  # Интересы (теги), несколько значений
        tags = request.POST.getlist('tags[]')  # Интересы (теги), несколько значений
        # tag1 = tags[0]
        city = request.POST.get('city')  # Город
        location = request.POST.get('location')  # Место проведения
        date = request.POST.get('date')  # Дата мероприятия
        start_time = request.POST.get('start-time')  # Время начала
        end_time = request.POST.get('end-time')  # Время окончания
        min_participants = request.POST.get('min-participants')  # Минимальное количество участников
        max_participants = request.POST.get('max-participants')  # Максимальное количество участников

        database = 'DB1.db'
        
        event_data = [date, start_time, end_time, theme, city, tags[0], " ", event_type, location]
        add_event(database, event_data)
        

        
        
        body = f"Приглашаем на мероприятие по теме: {tags[0]}!"
        subject = "Приглашение на событие"
        email_list = get_email_list(database, tags[0])
        
        sending_letters(email_list, body, subject)
        
        return HttpResponse(f'Имя: {event_data[0]}, Email: {event_data[1]}')

    else:
        # Если метод запроса не POST, отображаем пустую форму
        return render(request, 'myapp/event.html')
    
