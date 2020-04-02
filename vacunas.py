# Brayan Elgueta
# Kevin Oviedo
# Ignacio Rodriguez

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
def vacunas(): #funcion para listar las vacunas de nuestra base de datos
	cursor = mysql.get_db().cursor() #llamada a la base de datos	
	cursor.execute("SELECT * FROM vacuna") #consulta sql
	vacunas = cursor.fetchall()


	return render_template("vacunas.html", vacuneitor = vacunas) #retorna a la vista vacunas.html



@app.route('/agregarVacunas', methods=["POST"])
def vacunaNueva(): #funcion para agregar una nueva vacuna a nuestra base de datos
	cursor = mysql.get_db().cursor()
	try:
        #se crean variables para guardar nuestros datos ingresados en nuestro formulario segun el "name"
        #que se les haya asignado
		ahora = datetime.now()
		fecha = ahora.strftime("%Y-%m-%d")
		nombre = request.form["nombre"]
		sql = "INSERT INTO vacuna (nombre_enfermedad, fecha_ingreso) VALUES (%s,%s)"
		cursor.execute(sql,(nombre,fecha))

	except Exception as e:
		print(e)	
		
	return redirect(url_for('vacunas')) #retorna a la vista vacunas

@app.route('/', methods=["POST"])
def pacienteNuevo(): #se agrega un nuevo paciente a nuestra base de datos
	cursor = mysql.get_db().cursor()
	try:
		#se crean variables para guardar nuestros datos ingresados en nuestro formulario segun el "name"
        #que se les haya asignado
		rut = request.form["rut"]
		nombre = request.form["nombre"]
		fecha_nacimiento = request.form["fecha_nacimiento"]
		sql = "INSERT INTO paciente (rut, nombre, fecha_nacimiento) VALUES (%s,%s,%s)"#consulta SQL de ingreso
		cursor.execute(sql,(rut, nombre, fecha_nacimiento))

	except Exception as e:
		print(e)	
		
	return redirect(url_for('pacientes'))

@app.route('/pacientes')
def pacientes(): #funcion para listar los pacientes de nuestra base de datos
	cursor = mysql.get_db().cursor() #llamada a la base de datos	
	cursor.execute("SELECT * FROM paciente") #consulta sql
	pacientes = cursor.fetchall()


	return render_template("pacientes.html", pacients = pacientes)


@app.route('/vacunasPaciente/<string:rut>') #se rescata el rut para poder traspasarlo por medio de URL
def vacunasP(rut): #funcion para listar las vacunas que tiene un paciente en particular
	cursor = mysql.get_db().cursor()
	#consulta sql para mostrar solo las vacunas del paciente en particular
	cursor.execute("SELECT P.nombre, V.nombre_enfermedad, R.fecha_vacunacion  FROM paciente P, recibe R, vacuna V WHERE P.rut = R.rut_paciente AND R.cod_vacuna = V.cod_vacuna AND P.rut = %s",(rut))
	vervacunas = cursor.fetchall()
    
    #consulta sql para almacenar el nombre del paciente en particular
	cursor.execute("SELECT nombre FROM paciente WHERE rut = %s", (rut))
	nombre = cursor.fetchall()
    
    #nos lleva a la vista vacunasPaciente
	return render_template("vacunasPaciente.html", vacuns = vervacunas, nombres = nombre)

@app.route('/pacientesVacuna/<string:cod_vacuna>') #se rescata el codigo de la vacuna para poder traspasarlo
                                                   #por medio de URL
def verPacientes(cod_vacuna): #funcion para listar los pacientes que tiene una vacuna en particular
    cursor = mysql.get_db().cursor()

    #consulta sql para mostrar solo los pacientes que tienen una vacuna en particular
    cursor.execute("SELECT P.nombre, R.fecha_vacunacion FROM paciente P, recibe R, vacuna V WHERE P.rut = R.rut_paciente AND R.cod_vacuna = V.cod_vacuna AND V.cod_vacuna = %s",(cod_vacuna))	
    pacientesAll = cursor.fetchall()

    cursor.execute("SELECT nombre_enfermedad FROM vacuna WHERE cod_vacuna = %s",(cod_vacuna))
    vacunaN = cursor.fetchall()
    
    #nos lleva a la vista pacientesVacuna
    return render_template("pacientesVacuna.html", vpac = pacientesAll, vacunas = vacunaN)


@app.route('/mostrarDatos/<string:rut>') #se rescata el rut para poder traspasarlo por medio de URL
def mostrarDatos(rut): #funcion para mostrar los datos del paciente seleccionado y rescatar los datos
                       #almacenados en la tabla vacuna

	cursor = mysql.get_db().cursor()
	cursor.execute("SELECT cod_vacuna, nombre_enfermedad  FROM vacuna ")
	vervacunas = cursor.fetchall()

	cursor.execute("SELECT rut, nombre, fecha_nacimiento FROM paciente WHERE rut = %s", (rut))
	paciente = cursor.fetchall()




	return render_template("vacunarPacientes.html", vacunss = vervacunas, patiens = paciente)
	

@app.route('/vacunar/<string:rut>', methods=["POST"]) #se rescata el rut para poder traspasarlo por URL
def vacunarP(rut): #funcion para guardar los datos en la tabla recibe de nuestra base de datos
	cursor = mysql.get_db().cursor() 
	ahora = datetime.now() #se guarda la fecha actual en la que se hace el ingreso
	fecha_vacunacion = ahora.strftime("%Y-%m-%d") #se cambia el formato de muestra de la fecha
	cod_vacuna = request.form["nombre_enfermedad"] 

	#consulta SQL para ingresar en la tabla "recibe" de nuestra base de datos
	sql = "INSERT INTO recibe (rut_paciente, cod_vacuna, fecha_vacunacion) VALUES (%s,%s,%s)"
	cursor.execute(sql,(rut,cod_vacuna,fecha_vacunacion))
	
	return redirect(url_for('pacientes'))


if __name__ == "__main__":
	app.run(debug=True)

