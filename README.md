# hakaton

# Активировать виртуальную среду
source .venv/bin/activate
# Запуск локального сервера
python3 manage.py runserver
# Запуск бота в телеграмм
python3 bot.py


# Используемые библиотеки(установить, если не используется виртуальная среда)
# Установка виртуального окружения
python3 -m venv .venv --prompt VirtualEnv
# Установить библиотеки
python3 -m pip install -U beautifulsoup4
python3 -m pip install -U django
python3 -m pip install -U pyTelegramBotAPI
# Деактивировать виртуальную среду
deactivatea
