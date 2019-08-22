from flask import Flask, jsonify, render_template
from flask import request
from jinja2 import Template
import pymysql
import os

con = pymysql.connect("localhost", "root", "", "sap")
app = Flask(__name__, template_folder="mytemplate")
cf_port = os.getenv("PORT")

cur = con.cursor()
cur.execute("SELECT * FROM matmas")
data2 = cur.fetchall()

@app.route('/')
def display():
    
    return render_template("template2.html", data2=data2)

@app.route('/processjson', methods = ['POST'])
def processjson():
    data = request.get_json()
    count=0
    while(count<1000):
        count += 1
        for data_form in data:
           matnr = data_form["matnr"]
           maktx = data_form["maktx"]
           matkl = data_form["matkl"]
           ktmng = data_form["ktmng"]
           peinh = data_form["peinh"]   
           cursor = con.cursor()
           sql = "INSERT INTO matmas(matnr,maktx,matkl,ktmng,peinh) VALUES (%s,%s,%s,%s,%s)"
           val = (matnr,maktx,matkl,ktmng,peinh)
           cursor.execute(sql, val)
           con.commit()
           results = cursor.fetchall()
        return jsonify({'result' : 'Success!', 'matnr' : matnr, 'maktx' : maktx, 'matkl' : matkl, 'ktmng' : ktmng, 'peinh' : peinh})

#if __name__ == '__main__':
#  app.run(host='0.0.0.0',debug=True)
if __name__ == '__main__':
   if cf_port is None:
       app.run(host='0.0.0.0', port=5000)
   else:
       app.run(host='0.0.0.0', port=int(cf_port))    
