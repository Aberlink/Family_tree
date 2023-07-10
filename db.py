import psycopg2

import datetime



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


# cur.execute("INSERT INTO person (id, name, surname, birth) VALUES (%s, %s, %s, %s)", \
#     ("x7ald", "john", "smith", datetime.date(1995, 8, 12)))

# cur.execute("INSERT INTO relation (person_id_a, person_id_b, type) VALUES (%s, %s, %s)", \
#     ("x7ald", "x7ad", "siblings"))
# # DB.commit()

# cur.execute("SELECT * FROM relation;")
# x = cur.fetchall()
# print(x)

# for record in cur:
#     print(record)