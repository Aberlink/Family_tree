import psycopg2
import json

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


DB_con = create_conn(conf)
curr = DB_con.cursor()

