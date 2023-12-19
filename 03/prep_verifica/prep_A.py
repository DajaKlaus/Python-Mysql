import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Portiere20_05",
    database = "Animali"
)

mycursor = mydb.cursor()

mycursor.execute("""
                        CREATE TABLE Mammiferi(
                            id int NOT NULL,
                            Nome_Proprio varchar(255),
                            Razza varchar(255),
                            Peso int,
                            Eta int
                        )
                 """)