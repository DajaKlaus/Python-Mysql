import json
from flask_cors import CORS
import mysql.connector
from flask import Flask, jsonify

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Portiere20_05",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/air_transportHtml")
def air_transport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport = 'Air'")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/epic_unitsHtml")
def epic_units():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = 'Epic'")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/speed_unitsHtml")
def speed_units():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Speed = 'Medium (60)'")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/costHtml")
def cost():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost = '4'")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)