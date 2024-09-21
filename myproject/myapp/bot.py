# name: HakatonBot
# username: @Krona_s21_hakaton_bot
# token: 7388672440:AAFJZYvdTQ69Ojjr9mE8jrMDCuQv1Dg6FPI

import telebot
import sqlite3
import time
from threading import Thread

bot = telebot.TeleBot('7388672440:AAFJZYvdTQ69Ojjr9mE8jrMDCuQv1Dg6FPI')

user_phone: str = ''
user_telegram_id = 0
database2 = '../DB1.db'

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Введите свой номер телефона")
        bot.register_next_step_handler(message, get_phone)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

def get_phone(message):
    global user_phone, user_telegram_id, database2
    user_phone  = message.text
    user_telegram_id = message.from_user.id
    bot.send_message(message.from_user.id, f"Вы подписаны на события.")

    spisok = [user_phone, user_telegram_id]
    add_tele_id(database2, spisok)

    bot.send_message(message.from_user.id, "Ваши данные добавлены. Сессия завершена. Введите /start, чтобы начать заново.")

def add_tele_id(database2: str, tele_id: list[str]):
    
    connection = sqlite3.connect(database2)
    cursor = connection.cursor()

    query = f"insert into Telegram (Phone, TG_id) values (?, ?);"
    try:
        cursor.execute(query, (tele_id[0], tele_id[1]))
        print(f"OK")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

    connection.commit()
    connection.close()

def get_event(database2: str):
    connection = sqlite3.connect(database2)
    cursor = connection.cursor()
    
    query = f'SELECT * FROM Events ORDER BY id DESC LIMIT 1'
    cursor.execute(query)
    events = cursor.fetchone()

    connection.close()

    return list(events) if events else []


def get_users(database2: str, tag: str):

    connection = sqlite3.connect(database2)
    cursor = connection.cursor()

    query = f"""
        SELECT Telegram.TG_id
        FROM Telegram
        join (
            select users.Phone
            from Users
            join {tag} on {tag}.id_user = Users.id) AS temp on Telegram.Phone = temp.Phone
    """

    cursor.execute(query)
    tg_id = cursor.fetchall()
    tg_id_list = [elem[0] for elem in tg_id]

    connection.close()

    if tg_id:
        return tg_id_list
    else:
        return []


def broadcast_message(message_text, tag: str):

    global database2
    users = get_users(database2, tag)

    for user in users:
        try:
            bot.send_message(user, message_text)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с ID {user}: {e}")


def event_listener():
    global database2

    connection = sqlite3.connect(database2)
    cursor = connection.cursor()

    query = f'select max(id) from "Events";'
    cursor.execute(query)
    temp = cursor.fetchone()
    last_event_id = temp[0]

    connection.close()

    while True:
        event = get_event(database2)

        if event and (last_event_id is None or event[0] > last_event_id):
            last_event_id = event[0]
            event_name = event[4]
            broadcast_message(f'new event {event_name}', event[6])
        time.sleep(5)


def run_bot():
    bot.polling()

if __name__ == '__main__':

    Thread(target=run_bot).start()
    event_listener()