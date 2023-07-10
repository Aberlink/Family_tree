import json
import datetime as dt

from db import create_conn
from person import Person

with open('db_login.json') as login:
    conf = json.load(login)

DB = create_conn(conf)
cur = DB.cursor()


mp = Person("kasia", "mysz", dt.date(1995, 8, 12))
# mp.push_to_db(DB)
mp.kill(dt.date(2020,1,10))
print(mp)

# cur.execute("SELECT * FROM person;")
# x = cur.fetchall()
# print(x)

DB.close()
cur.close()

