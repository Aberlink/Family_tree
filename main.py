import psycopg2
import json
import datetime

with open('db_login.json') as login:
    conf = json.load(login)

def create_conn(config):
    try:
        conn=psycopg2.connect(dbname = config['dbname'],
                            host = config['host'],
                            port = config['port'],
                            user = config['user'],
                            password = config['password'])
    except Exception as err:
        print(err.code, err)
    return conn


DB = create_conn(conf)
cur = DB.cursor()


cur.execute("INSERT INTO person (id, name, surname, birth) VALUES (%s, %s, %s, %s)", \
    ("x7ald", "john", "smith", datetime.date(1995, 8, 12)))
DB.commit()

cur.execute("SELECT * FROM person;")
for record in cur:
    print(record)

DB.close()
cur.close()

