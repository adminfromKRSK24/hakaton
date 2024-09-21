class TempUserData:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        # Импорт модели UserData и сохранение данных в базу
        from .models import UserData
        user_data = UserData(name=self.name, email=self.email)
        user_data.save()

        return user_data
