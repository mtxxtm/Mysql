import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="eusav23233",
  database="mydatabase"
)

mycursor = mydb.cursor()
#run sql commands
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
