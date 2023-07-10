import datetime as dt
import uuid

class Person:
    def __init__(self, name, surname, birth, p_id=uuid.uuid4(), death=None):
        self.p_id = str(p_id)
        self.name = name
        self.surname = surname
        self.birth = birth
        self.death = death
        
    
    def __str__(self):
        return f"p_id: {self.p_id}, Name: {self.name}, surname: {self.surname}, birth: {self.birth}, death: {self.death}"
    
    def push_to_db(self, db):
        query = "INSERT INTO person (id, name, surname, birth, death) VALUES (%s, %s, %s, %s, %s)"
        data = (self.p_id, self.name, self.surname, self.birth, self.death)

        try:
            with db.cursor() as cur:
                cur.execute(query, data)
            db.commit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
    def kill(self, death_date):
        self.death = death_date
        
        
    def is_adult(self, reference=dt.datetime.today().date()):
        age = reference.year - self.birth.year
        compare = dt.date(reference.year, self.birth.month, self.birth.day)
        if reference < compare:
            age -= 1
        return age >= 18

        
        