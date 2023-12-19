import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Portiere20_05",
    database = "Animali"
)

mycursor = mydb.cursor()

mycursor.execute("""select * 
                    from mammiferi
                    where Peso > 2""")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)