# hakaton

# Установка виртуального окружения
python3 -m venv .venv --prompt VirtualEnv
# Активировать виртуальную среду
source .venv/bin/activate
# Деактивировать виртуальную среду
deactivatea
# Установить библиотеки
python3 -m pip install -U beautifulsoup4
python3 -m pip install -U django
python3 -m pip install -U pyTelegramBotAPI

# Запуск локального сервера
python3 manage.py runserver
# Запуск бота в телеграмм
python3 ./myapp/bot.py