import asyncio

import aiopg.sa
import psycopg2
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

__all__ = ['question', 'choice', 'init_pg', 'close_pg']

meta = MetaData()

question = Table(
    'question', meta,

    Column('id', Integer, primary_key=True),
    Column('question_text', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)

choice = Table(
    'choice', meta,

    Column('id', Integer, primary_key=True),
    Column('choice_text', String(200), nullable=False),
    Column('votes', Integer, server_default="0", nullable=False),

    Column('question_id',
           Integer,
           ForeignKey('question.id', ondelete='CASCADE'))
)


async def init_pg(app):
    """ Connect to the PostgreSQL database server """
    engine = psycopg2.connect(
    host="localhost",
    database="aiohttpdemo_polls",
    user="aiohttpdemo_user",
    password="aiohttpdemo_pass")
    print('first message')
    cursor = engine.cursor()
    cursor.execute("SELECT question_text FROM question")
    results = cursor.fetchall()
    print(results)
    app['db'] = engine
    print(engine)

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()

