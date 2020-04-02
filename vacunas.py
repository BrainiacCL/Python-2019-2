import requests
from flask import Flask, render_template, jsonify, request, url_for, redirect
from flaskext.mysql import MySQL
from datetime import date
from datetime import datetime
import pymysql
import pymysql.cursors

app = Flask(__name__)

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"] = "vacunas"

mysql = MySQL(app)
mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor


@app.route('/vacunas')
def vacunas():
	cursor = mysql.get_db().cursor() #llamada a la base de datos	
	cursor.execute("SELECT * FROM vacuna") #consulta sql
	vacunas = cursor.fetchall()


	return render_template("vacunas.html", vacuneitor = vacunas)



@app.route('/agregarVacunas', methods=["POST"])
def vacunaNueva():
	cursor = mysql.get_db().cursor()
	try:

		ahora = datetime.now()
		fecha = ahora.strftime("%Y-%m-%d")
		nombre = request.form["nombre"]
		sql = "INSERT INTO vacuna (nombre_enfermedad, fecha_ingreso) VALUES (%s,%s)"
		cursor.execute(sql,(nombre,fecha))

	except Exception as e:
		print(e)	
		
	return redirect(url_for('vacunas'))

@app.route('/', methods=["POST"])
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


@app.route('/vacunasPaciente/<string:rut>')
def vacunasP(rut):
	cursor = mysql.get_db().cursor()
	cursor.execute("SELECT P.nombre, V.nombre_enfermedad, R.fecha_vacunacion  FROM paciente P, recibe R, vacuna V WHERE P.rut = R.rut_paciente AND R.cod_vacuna = V.cod_vacuna AND P.rut = %s",(rut))
	vervacunas = cursor.fetchall()

	cursor.execute("SELECT nombre FROM paciente WHERE rut = %s", (rut))
	nombre = cursor.fetchall()

	return render_template("vacunasPaciente.html", vacuns = vervacunas, nombres = nombre)

@app.route('/pacientesVacuna/<string:cod_vacuna>')
def verPacientes(cod_vacuna):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT P.nombre, R.fecha_vacunacion FROM paciente P, recibe R, vacuna V WHERE P.rut = R.rut_paciente AND R.cod_vacuna = V.cod_vacuna AND V.cod_vacuna = %s",(cod_vacuna))	
    pacientesAll = cursor.fetchall()

    cursor.execute("SELECT nombre_enfermedad FROM vacuna WHERE cod_vacuna = %s",(cod_vacuna))
    vacunaN = cursor.fetchall()

    return render_template("pacientesVacuna.html", vpac = pacientesAll, vacunas = vacunaN)

if __name__ == "__main__":
	app.run(debug=True)

