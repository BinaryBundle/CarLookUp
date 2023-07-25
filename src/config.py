from dotenv import load_dotenv

import os

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BASE_DIR = os.path.abspath(os.getcwd())
ADMINS = list(map(int, os.environ.get('ADMINS').split(',')))

PSQL_DB_USER = os.environ.get('PSQL_DB_USER')
PSQL_DB_PASSWORD = os.environ.get('PSQL_DB_PASSWORD')
PSQL_DB_HOST = os.environ.get('PSQL_DB_HOST')
PSQL_DB_NAME = os.environ.get('PSQL_DB_NAME')
