import json
from flask_cors import CORS
import mysql.connector
from flask import Flask

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Portiere20_05",
  database="F1"
)
mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM F1.F1_data")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/circuitRefHtml")
def circuitRef():
    mycursor.execute("SELECT circuitRef FROM F1.F1_data")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/circuitRef_countryHtml")
def circuitRef_country():
    mycursor.execute("SELECT circuitRef, country FROM F1.F1_data")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/circuitRef_nameHtml")
def circuitRef_name():
    mycursor.execute("SELECT circuitRef, name FROM F1.F1_data")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)

@app.route("/circuitRef_locationHtml")
def circuitRef_location():
    mycursor.execute("SELECT circuitRef, location FROM F1.F1_data")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(dict(zip(row_headers, x)))
        print(result)
    return json.dumps(result)
