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

val = []

for i in range(5):
    tuple = ()
    print("\nNuova tupla")
    for j in range(5):
        x = input("Inserisci valore: ")
        tuple += (x,)
    val.append(tuple)


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
