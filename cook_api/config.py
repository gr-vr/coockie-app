import os
from dotenv import load_dotenv


class Settings:
    ENV = os.environ.get('ENV', 'DEV')

    if ENV == 'DEV':
        load_dotenv('../.env')

    PORT = int(os.environ.get('PORT', 5000))
    DB_URI = os.environ.get('DB_URI')
