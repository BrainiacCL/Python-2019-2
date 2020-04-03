-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 02-04-2020 a las 22:31:10
-- Versión del servidor: 5.7.24
-- Versión de PHP: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `vacunas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

DROP TABLE IF EXISTS `paciente`;
CREATE TABLE IF NOT EXISTS `paciente` (
  `rut` varchar(12) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  PRIMARY KEY (`rut`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`rut`, `nombre`, `fecha_nacimiento`) VALUES
('19.425.846-1', 'Kevin Oviedo', '1996-08-06'),
('15.426.845-1', 'Marcelo Oses', '2020-04-22'),
('19.425.236-1', 'Karla Martinez', '2020-03-31'),
('12.254.369-5', 'Javier Insunsa', '1980-04-07'),
('15.353.567-1', 'Jose Munoz', '1980-10-30'),
('11.333.543-4', 'Maria Jesus', '1989-02-07'),
('20.455.675-3', 'Nathaly Agui', '2011-04-07'),
('19.443.523-0', 'Alfonso Klen', '2012-07-17'),
('20.212.233-3', 'Bastian Weas', '2000-10-22'),
('17.563.427-4', 'Naeri Molado', '2000-06-07'),
('18.423.578-1', 'Fabian Lopez', '1987-10-07'),
('16.334.567-1', 'Esteban Garcia', '1965-12-07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recibe`
--

DROP TABLE IF EXISTS `recibe`;
CREATE TABLE IF NOT EXISTS `recibe` (
  `rut_paciente` varchar(12) NOT NULL,
  `cod_vacuna` bigint(20) NOT NULL,
  `fecha_vacunacion` date DEFAULT NULL,
  PRIMARY KEY (`rut_paciente`,`cod_vacuna`),
  KEY `cod_vacuna` (`cod_vacuna`),
  KEY `rut_paciente` (`rut_paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `recibe`
--

INSERT INTO `recibe` (`rut_paciente`, `cod_vacuna`, `fecha_vacunacion`) VALUES
('11.333.543-4', 1, '2020-04-02'),
('11.333.543-4', 2, '2020-04-02'),
('11.333.543-4', 5, '2020-04-02'),
('11.333.543-4', 10, '2020-04-02'),
('12.254.369-5', 8, '2020-04-02'),
('12.254.369-5', 9, '2020-04-02'),
('15.353.567-1', 5, '2020-04-02'),
('15.426.845-1', 9, '2020-04-02'),
('16.334.567-1', 3, '2020-04-02'),
('17.563.427-4', 4, '2020-04-02'),
('17.563.427-4', 7, '2020-04-02'),
('18.423.578-1', 10, '2020-04-02'),
('19.425.236-1', 6, '2020-04-02'),
('19.425.846-1', 4, '2020-04-02'),
('19.425.846-1', 6, '2020-04-02'),
('19.443.523-0', 7, '2020-04-02'),
('19.443.523-0', 8, '2020-04-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacuna`
--

DROP TABLE IF EXISTS `vacuna`;
CREATE TABLE IF NOT EXISTS `vacuna` (
  `cod_vacuna` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_enfermedad` varchar(255) DEFAULT NULL,
  `fecha_ingreso` date DEFAULT NULL,
  PRIMARY KEY (`cod_vacuna`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `vacuna`
--

INSERT INTO `vacuna` (`cod_vacuna`, `nombre_enfermedad`, `fecha_ingreso`) VALUES
(1, 'Varicela', '2020-04-02'),
(2, 'Tétano', '2020-04-02'),
(3, 'Sarampión', '2020-04-02'),
(4, 'Rotavirus', '2020-04-02'),
(5, 'Polio', '2020-04-02'),
(6, 'Tos ferina (Pertusis)', '2020-04-02'),
(7, 'Gripe (Influenza)', '2020-04-02'),
(8, 'Hepatitis B', '2020-04-02'),
(9, 'Hepatitis A', '2020-04-02'),
(10, 'Difteria', '2020-04-02');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
