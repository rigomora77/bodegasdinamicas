-- Registro de creacion de base de datos

-- Tabla de nombre de bodegas dinamicas

CREATE TABLE IF NOT EXISTS stores(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  code INT UNSIGNED NOT NULL UNIQUE,
  name VARCHAR(80) NOT NULL,
  PRIMARY KEY(id)
);

-- Insertar informacion

INSERT INTO stores (code, name) VALUES (503,'mayca');
INSERT INTO stores (code, name) VALUES (504,'frionet');

-- Ver esquema de la tabla

DESC stores;

-- Hacer consulta de la tabla

SELECT * FROM stores;

-- Tabla de numeros de parte

CREATE TABLE IF NOT EXISTS parts(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  sap_code VARCHAR(16) NOT NULL UNIQUE,
  sup_cod VARCHAR(30) NOT NULL,
  name VARCHAR(150) NOT NULL,
  qty DECIMAL NOT NULL,
  PRIMARY KEY(id)
);

-- Insertar informacion

INSERT INTO parts(sap_code, sup_cod, name, qty) VALUES ('CRRE00091496','115032-302-88', 'RUEDA DE CARGA CON ROLES 5.00 X 2.88', 0);
INSERT INTO parts(sap_code, sup_cod, name, qty) VALUES ('CRRE00123111','121501-348-01', 'RUEDA DE TRACCIÓN LISA 13X5.5-9.5', 0);

-- falta agregar tabla de stockrooms