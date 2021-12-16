drop database db_poo;

create database db_pedidos;

use db_pedidos;

CREATE TABLE pedidos (
  id int(5) NOT NULL primary key auto_increment,
  producto varchar(50) NOT NULL,
  cantidad int(5) NOT NULL,
  tipo varchar(50) NOT NULL
  fecha varchar(10)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into pedidos(producto,cantidad,tipo,fecha)
values ('','999888777','jaime@abc.com');
