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

    # def add_user(database: str, user: list[str]):
    #     connection = sqlite3.connect(database)
    #     cursor = connection.cursor()

    #     query = f"insert into users (Surname, Second_name, Phone, Email) values ('{user[0]}', '{user[1]}', '{user[2]}', '[{user[3]}]');"
    #     cursor.execute(query)

    #     connection.commit()
    #     connection.close()