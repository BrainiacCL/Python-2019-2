CREATE TABLE paciente(
	rut VARCHAR(12) NOT NULL,
	nombre VARCHAR(255),
	fecha_nacimiento DATE,
	PRIMARY KEY(rut)
);

CREATE TABLE vacuna(
	cod_vacuna bigint NOT NULL,
	nombre_enfermedad VARCHAR(255),
	fecha_ingreso DATE,
	PRIMARY KEY (cod_vacuna)
);

CREATE TABLE recibe(
	rut_paciente VARCHAR(12) NOT NULL,
	cod_vacuna bigint NOT NULL,
	fecha_vacunacion DATE,
	PRIMARY KEY(rut_paciente,cod_vacuna),
	FOREIGN KEY(rut_paciente) REFERENCES paciente (rut),
	FOREIGN KEY(cod_vacuna) REFERENCES vacuna (cod_vacuna)
);