CREATE DATABASE usuarios_db;

USE usuarios_db;

CREATE TABLE departamentos(
	id VARCHAR(5) NOT NULL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE usuarios(
	nombre VARCHAR(25) NOT NULL,
    apellido VARCHAR(25) NOT NULL,
    nombreUsuario VARCHAR(25) NOT NULL PRIMARY KEY,
    password VARCHAR(150) NOT NULL,
    id_departamento VARCHAR(5),
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id)
);

INSERT INTO departamentos(id,nombre)
VALUES ('TI-01','Desarrollo Web'),
		('TI-02','Desarrollo de Hardware'),
        ('TI-03','Desarrollo de Software'),
        ('LY-01','Leyes');

select * from departamentos;

select * from usuarios;

SELECT * FROM departamentos d, usuarios u WHERE d.id = u.id_departamento;
SELECT * FROM departamentos d
LEFT JOIN usuarios u ON d.id = u.id_departamento;


SELECT * FROM usuariosfriends
WHERE nombreUsuario = 'Garavito94' AND password = '123456'