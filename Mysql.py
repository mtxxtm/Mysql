#imports mysql
import mysql.connector
#connection to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="eusav23233"
)
#create cursor
mycursor = mydb.cursor()
#execute the command
mycursor.execute("CREATE DATABASE mydatabase")
