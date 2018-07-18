import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, send_file
from io import StringIO
import io
import matplotlib.pyplot as plt
import urllib
import json
import datetime
# from bson import json_util

app = Flask(__name__)
app.debug = True


@app.route('/fig')
def fig():
      plt.plot([1,2,3,4], [1,2,3,4])
      img = io.BytesIO()
      plt.savefig(img, format='png')
      img.seek(0)
      plot_data = urllib.quote(base64.b64encode(img.read()).decode())
      return send_file(img, plot_url=plot_data)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def dbconnect():
    try:
      cnx = mysql.connector.connect(user="root",
                                    host="localhost", 
                                    database="sys")
    except mysql.connector.Error as err:
        return (err.msg)
    else:
      return cnx

@app.route("/SST")
def temp():
    db = dbconnect()
    try:
        cur = db.cursor()
    except:
        return json.dumps({ "error": db }), 500
    
    query = "show tables"
    try:
    	cur.execute(query)
    except mysql.connector.Error as err:
    	print(err)
    	return json.dumps({ "error" :err.msg}), 500

    col_names=cur.column_names
    rv = cur.fetchall()
    json_data =[]
    for result in rv:
        json_data.append(dict(zip(col_names,result)))
    db.close()
    print(len(json_data))
    return json.dumps([json_data, col_names], default = myconverter)

@app.route("/SST-PAM")
def temp1():
    db = dbconnect()
    try:
        cur = db.cursor()
    except:
        return json.dumps({ "error": db }), 500
    
    # query = "select * from FILELOG"
    query = "show table status"
    try:
    	cur.execute(query)
    except mysql.connector.Error as err:
    	print(err)
    	return json.dumps({ "error" :err.msg}), 500

    col_names=cur.column_names
    rv = cur.fetchall()
    json_data =[]
    for result in rv:
        json_data.append(dict(zip(col_names,result)))
    db.close()
    return json.dumps([json_data, col_names], default = myconverter)

@app.route("/SST-GX")
def temp2():
    db = dbconnect()
    try:
        cur = db.cursor()
    except:
        return json.dumps({ "error": db }), 500
    
    query = "SHOW TABLES"
    try:
    	cur.execute(query)
    except mysql.connector.Error as err:
    	print(err)
    	return json.dumps({ "error" :err.msg}), 500

    col_names=cur.column_names
    rv = cur.fetchall()
    json_data =[]
    for result in rv:
        json_data.append(dict(zip(col_names,result)))
    db.close()
    return json.dumps([json_data, col_names], default = myconverter)

@app.route("/SST-SHARE")
def temp3():
    db = dbconnect()
    try:
        cur = db.cursor()
    except:
        return json.dumps({ "error": db }), 500
    
    query = "SHOW VARIABLES"
    try:
    	cur.execute(query)
    except mysql.connector.Error as err:
    	print(err)
    	return json.dumps({ "error" :err.msg}), 500

    col_names=cur.column_names
    rv = cur.fetchall()
    json_data =[]
    for result in rv:
        json_data.append(dict(zip(col_names,result)))
    db.close()
    return json.dumps([json_data, col_names], default = myconverter)


if __name__ == "__main__":
    app.run()