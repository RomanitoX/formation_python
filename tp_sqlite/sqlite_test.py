import sqlite3
from random import randint

from faker import Faker

fake = Faker(locale="fr-FR")

conn = sqlite3.connect("tp_sqlite/database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text,
    salaire int
)
""")

"""for _ in range(10):
    d= {"prenom" : fake.first_name(), "nom" : fake.last_name(), "salaire" : randint(0, 50000)} 
    c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)"""
    


c.execute("SELECT * FROM employees")
data = c.fetchall()
print(data)

conn.commit()
conn.close()