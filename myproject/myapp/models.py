from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'users'  # Указываем имя существующей таблицы
        db_table = 'Event'
        managed = False  # Отключаем миграции для этой модели
