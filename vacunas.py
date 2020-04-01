import requests
from flask import Flask, render_template, jsonify, request
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors

app = Flask(__name__)

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"] = "pacientes"

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor


@app.route('/pacientes')
def pacientes():
	cursor = mysql.get_db().cursor() #llamada a la base de datos	
	cursor.execute("SELECT * FROM paciente") #consulta sql
	pacientes = cursor.fetchall()


	return render_template("vacunas.html", pacients = pacientes)


if __name__ == "__main__":
	app.run(debug=True)

