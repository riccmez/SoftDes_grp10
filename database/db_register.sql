mysql -u root -p.
drop database db_poo;

create database db_mails;

use db_mails;

CREATE TABLE ventas (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  categoria varchar(50) NOT NULL,
  cantidad varchar(50) NOT NULL,
  cliente varchar(50) NOT NULL,
  estado varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into ventas(nombre,categoria, cantidad, cliente ,estado)
values ('The Batman','coleccionable','1','jaime@gmail.com','Entregado');
