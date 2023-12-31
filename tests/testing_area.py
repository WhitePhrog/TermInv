import mysql.connector


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "!180804Ococchiste",
)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

print(mycursor)