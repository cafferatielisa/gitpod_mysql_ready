import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #locazione
  user="root",    
  password=""
)

mycursor = mydb.cursor()  #crea un cursore su phyton che scrive nel cursore di sql

mycursor.execute("CREATE DATABASE mydatabase")  #scrive al nostro posto in sql, grazie al cursone