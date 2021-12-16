drop database db_poo;

create database db_prod;

use db_prod;

CREATE TABLE productos (
  id int(5) NOT NULL primary key auto_increment,
  producto varchar(50) NOT NULL,
  cantidad int(5) NOT NULL,
  tipo varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into productos(producto,cantidad,tipo)
values ('Jaime','999888777','jaime@abc.com');
