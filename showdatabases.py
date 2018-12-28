import mysql.connector
#database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="eusav23233",
)
mycursor = mydb.cursor()
#below line shows databases
mycursor.execute("SHOW DATABASES")
#shows all data bases
for x in mycursor:
  print(x)
