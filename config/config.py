import os
from dotenv import load_dotenv

# загрузка переменных окружения из .env файла
load_dotenv()
# Получаем токен бота из .env файла
TOKEN = str(os.getenv('BOT_TOKEN'))
