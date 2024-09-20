# from django.db import models

# Эта модель будет представлять структуру таблицы в базе данных
# с двумя полями: name (имя пользователя) и email.
    # class UserData(models.Model):
    #     name = models.CharField(max_length=100)
    #     email = models.EmailField()

    #     def __str__(self):
    #         return f'{self.name} - {self.email}'

# myapp/models.py

from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'users'  # Указываем имя существующей таблицы
        managed = False  # Отключаем миграции для этой модели

class Event(models.Model):
    date = models.DateField()  # Дата мероприятия
    theme = models.CharField(max_length=200)  # Тема мероприятия
    city = models.CharField(max_length=100)  # Город
    type = models.CharField(max_length=100)  # Тип мероприятия
    location = models.CharField(max_length=200)  # Место проведения
    start_time = models.TimeField()  # Время начала мероприятия
    end_time = models.TimeField()  # Время окончания мероприятия
    tags = models.CharField(max_length=200)  # Тэги мероприятия

    class Meta:
        db_table = 'Event'  # Указываем имя таблицы

    def __str__(self):
        return f"{self.theme} - {self.date}"