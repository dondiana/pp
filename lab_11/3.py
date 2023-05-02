import psycopg2
from config import config

def insert_list(l):
    insert = """
    INSERT INTO phonebook(firstname, lastname, phonenumber) VALUES(%s, %s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(insert, (l))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = [
    ("name1", "surname1", "+7-222-111-22-11"),
    ("name2", "surname2", "+7-333-111-22-22"),
    ("name3", "surname3", "+7-555-000-22-11"),
]

insert_list(l)