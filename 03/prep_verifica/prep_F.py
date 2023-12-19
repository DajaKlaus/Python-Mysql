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

num_animali = int(input("Quanti animali si desidera inserire:\n"))

for i in range(num_animali):
    tuple = ()
    print("\nNuova tupla")
    for j in range(5):
        x = input("Inserisci valore: ")
        tuple += (x,)
    
    val.append(tuple)
    if num_animali > 1:
        scelta = input("\nContinuare?\n").lower()
        if scelta == "no":
            break
        else: 
            pass


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
