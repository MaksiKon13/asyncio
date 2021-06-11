import psycopg2
from aiohttp import web
import db
from psycopg2 import Error

# aiohttpdemo_polls/views.py
from aiohttp import web
from psycopg2.extras import NamedTupleCursor

async def index(request):
    connection = psycopg2.connect(
        host="localhost",
        database="aiohttpdemo_polls",
        user="aiohttpdemo_user",
        password="aiohttpdemo_pass")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    cursor.execute("SELECT * FROM question;")
    # Получить результат
    record = cursor.fetchone()
    cursor.execute("SELECT id FROM question;")
    # Получить результат
    record1 = str(cursor.fetchone())
    cursor.execute("SELECT * FROM question;")
    record2 = str(cursor.fetchall())
    return web.Response(
        text='\nЭтот Франкенштейн начал подавать признаки жизни\n\n' + str(
            record) + '\n' + str(record1)+'\n\n\n'+str(record2))


