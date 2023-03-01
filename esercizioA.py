import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #locazione
  user="root",    
  password="",
  database="Animali"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE mammiferi (id int, nome_proprio VARCHAR(255), razza VARCHAR(255), peso int, eta int)")