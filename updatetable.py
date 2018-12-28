import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="eusav23233",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN job VARCHAR(255)")
