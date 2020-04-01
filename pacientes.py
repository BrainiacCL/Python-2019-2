import requests
from flask import Flask, render_template, jsonify, request, url_for, redirect
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors

app = Flask(__name__)

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"] = "vacunas"

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor


@app.route('/nuevoPaciente', methods=["POST"])
def pacienteNuevo():
	cursor = mysql.get_db().cursor()
	try:

		rut = request.form["rut"]
		nombre = request.form["nombre"]
		fecha_nacimiento = request.form["fecha_nacimiento"]
		sql = "INSERT INTO paciente (rut, nombre, fecha_nacimiento) VALUES (%s,%s,%s)"
		cursor.execute(sql,(rut, nombre, fecha_nacimiento))

	except Exception as e:
		print(e)	
		
	return redirect(url_for('pacientes'))

@app.route('/pacientes')
def pacientes():
	cursor = mysql.get_db().cursor() #llamada a la base de datos	
	cursor.execute("SELECT * FROM paciente") #consulta sql
	pacientes = cursor.fetchall()


	return render_template("pacientes.html", pacients = pacientes)


@app.route('/vacunar')
def vacunacion():
	cursor = mysql.get_db().cursor()
	cursor.execute

if __name__ == "__main__":
	app.run(debug=True)

