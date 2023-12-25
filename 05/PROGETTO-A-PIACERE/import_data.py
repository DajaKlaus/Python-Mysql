# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Portiere20_05"
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS F1")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS F1.F1_data (
    circuitId VARCHAR(255) NOT NULL,
    circuitRef VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    lat VARCHAR(255) NOT NULL,
    lng VARCHAR(255) NOT NULL,
    alt VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    PRIMARY KEY (circuitId)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM F1.F1_data")
mydb.commit()

#Read data from a csv file
f1_data = pd.read_csv('./esercizi/05/PROGETTO-A-PIACERE/circuits.csv', index_col=False, delimiter = ',')
f1_data = f1_data.fillna('Null')
print(f1_data.head(20))

#Fill the table
for i,row in f1_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO F1.F1_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM F1.F1_data")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)