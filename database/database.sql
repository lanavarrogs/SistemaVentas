CREATE database construccion;
USE construccion;

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(60),
    email VARCHAR(50),
    edat INT,
    telefono VARCHAR(15),
    direccion VARCHAR (40)
);
S
CREATE TABLE trabajador(
    id_trabajador INT PRIMARY KEY,
    nombre VARCHAR(60),
    email VARCHAR(50),
    edad INT,
    telefono VARCHAR(15),
    direccion VARCHAR(15)
);

CREATE TABLE producto(
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(60),
    precio DOUBLE
);

CREATE TABLE ventas(
    id_venta INT PRIMARY KEY,
    estatus VARCHAR(40),
    total DOUBLE,
    sucursal VARCHAR(50),
    id_cliente INT,
    id_trabajador INT,
    id_producto INT,
    FOREIGN KEY (id_trabajador) REFERENCES trabajador(id_trabajador),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES trabajador(id_trabajador)
);


INSERT INTO cliente VALUES(1,'juan','juan@gmail.com',30,'55660012','norte 45 #1234');
INSERT INTO cliente VALUES(2,'miguel','miguel@gmail.com',32,'55661112','lomas verdes #4321');
INSERT INTO cliente VALUES(3,'paco','paco@gmail.com',40,'55662212','Reforma #12356');


INSERT INTO trabajador VALUES(1,'roberto','roberto@gmail.com',26,'55295629','Direcc #1234');
INSERT INTO trabajador VALUES(2,'manuel','manuel@gmail.com',26,'55295628','Direcc #1235');
INSERT INTO trabajador VALUES(3,'allison','allison@gmail.com',24,'55295627','Direcc #1236');

INSERT INTO producto VALUES(1,'Tablaroca',150.10);
INSERT INTO producto VALUES(2,'Cemento',.350.00);
INSERT INTO producto VALUES(3,'Pala premium',1600.00);

INSERT INTO ventas VALUES(1,'comprado',350.00,'Reforma',1,1,1)