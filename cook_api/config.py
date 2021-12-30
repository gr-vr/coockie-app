import os
from dotenv import load_dotenv


class Settings:
    ENV = os.environ.get('ENV', 'DEV')

    if ENV == 'DEV':
        load_dotenv('../.env')

    PORT = int(os.environ.get('PORT', 5000))
    TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    APP_URL = os.environ.get('APP_URL')
    FULL_URL = f'{APP_URL}{TOKEN}'
    DB_URI = os.environ.get('DB_URI')