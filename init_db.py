# polls/init_db.py
from sqlalchemy import create_engine, MetaData

from aiohttpdemo_polls.settings import config
from aiohttpdemo_polls.db import question, choice


DSN = "postgresql://maxim:password2@localhost:5432/polls_1"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'question_text': 'EVGEN, ZPAZIBBA!',
         'pub_date': '2021-06-06 21:20:49.629+02'}
    ])
    conn.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
