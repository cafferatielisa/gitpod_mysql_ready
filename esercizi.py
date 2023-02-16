import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #locazione
  user="root",    
  password="",
  database="Animali"
)

mycursor = mydb.cursor()  #crea un cursore su phyton che scrive nel cursore di sql
sql = "INSERT INTO Animali (id, nome_proprio, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
val =[
 ("2", "gatto", "certosino", "5", "15"),
 ("3", "cane", "barboncino", "3", "11"),
 ("4", "topo", "grigio", "1", "1"),
 ("5", "giraffa", "africana", "300", "2")
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")