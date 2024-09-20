import sqlite3


class Add:

    def __init__(self):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
    def add_user(self, database: str, user: list[str]):
        
        query = f"insert into users (Surname, Name, Phone, Email) values (?, ?, ?, ?);"
        try:
            self.cursor.execute(query, (user[0], user[1], user[2], user[3]))
            print(f"Событие добавлено.")
        except sqlite3.IntegrityError as e:
            print(f"Ошибка добавления события: {e}")

        self.connection.commit()
        self.connection.close()

    def add_event(self, database: str, event: list[str]):

        query = "insert into Event (date, time_start, time_end, Name, Place, Interes, Spiker) values (?, ?, ?, ?, ?, ?, ?);"

        try:
            self.cursor.execute(query, (event[0], event[1], event[2], event[3], event[4], event[5], event[6]))
            print(f"Событие добавлено.")
        except sqlite3.IntegrityError as e:
            print(f"Ошибка добавления события: {e}")

        self.connection.commit()
        self.connection.close()



if __name__ == '__main__':

    database = './db/DB1.db'
    event = Add()
    user = Add()

    add_event = ['2025-11-17', '17:25:00', '18:25:00', 'название', 'nsk', 'it', '10']
    add_user = ['Иванов', 'Иван', '8-953-000-00-12', 'abcdef@mail.ru']

    event.add_event(database, add_event)
    user.add_user(database, add_user)
