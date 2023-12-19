import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Portiere20_05",
    database = "Animali"
)

mycursor = mydb.cursor()

sql = """INSERT INTO Mammiferi (id, Nome_Proprio, Razza, Peso, Eta) 
         VALUES (%s, %s, %s, %s, %s)"""

val = [
        (1, "Josh", "German Shepherd", 30, 2),
        (2, "Pippo", 'Gatto Soriano', 5, 4),
        (3, 'Bubbles', 'Cavallo Quarter Horse', 500, 8),
        (4, 'Kai', 'Orca', 9000, 15),
        (5, 'Simba', 'Leone', 190, 6)
    ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")