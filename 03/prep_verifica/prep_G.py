import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "Portiere20_05",
    database = "Animali"
)

mycursor = mydb.cursor()

def inserisci():
    sql = """INSERT INTO Mammiferi (id, Nome_Proprio, Razza, Peso, Eta) 
         VALUES (%s, %s, %s, %s, %s)"""
    etichette = [col.strip() for col in sql.split("(")[1].split(")")[0].split(",")]
    val = []

    num_animali = int(input("\nQuanti animali si desidera inserire:\n"))

    for i in range(num_animali):
        tuple = ()
        print("\nNuova tupla")
        for label in etichette:
            x = input(f"Inserisci {label}: ")
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

def vis():
    mycursor = mydb.cursor()

    mycursor.execute("select * from mammiferi")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def elimina():
    i = int(input("\nInserisci id dell'animale da eliminare: "))

    sql = """DELETE FROM Mammiferi WHERE id = %s"""

    mycursor.execute(sql, (i,))
    mydb.commit()

    print(mycursor.rowcount, "record deleted.")

def modificare():
    pass

scelta_menu = int(input("""--------------------------------------------
1. Premi 1 per inserire un nuovo animale\n
2. Premi 2 per visualizzare tutti gli animali\n
3. Premi 3 per eliminare un animale\n
4. Premi 4 per modificare un animale
--------------------------------------------\n\n
->"""))

if scelta_menu == 1:
    inserisci()
elif scelta_menu == 2:
    vis()
elif scelta_menu == 3:
    elimina()
elif scelta_menu == 4:
    modificare()

mydb.commit()