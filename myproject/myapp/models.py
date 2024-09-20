from django.db import models

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
