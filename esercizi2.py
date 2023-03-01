import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #locazione
  user="root",    
  password="",
  database="Animali"
)
mycursor = mydb.cursor()
