mysql -u root -p

drop database db99;
show databases;
create database db99;
show databases;
use db99;

drop table Location;
create table Location
(
    id int not null  AUTO_INCREMENT primary key,
    landmark varchar(20) not null,
    city varchar(20),
    state varchar(20),
    country varchar(20),
    pincode int not null
)ENGINE=InnoDB CHARACTER SET utf8;
desc Location;
select * from Location;

insert into Location(landmark,city,state,country,pincode)
values
('LA1','Mumbai','maharastra','india',408303),
('LA11','Palghar','maharastra','india',405303),
('LA2','Pune','maharastra','india',401903),
('LA3','Nagpur','maharastra','india',409303);

select * from Location;
--Column count doesn't match value count at row 1
insert into Location
values
(111,'LA1','Mumbai','india',408303);


insert into Location(id,landmark,city,country,pincode)
values
(111,'LA1','Mumbai','india',408303);

insert into Location(id,landmark,city,state,country)
values
(117,'LA1','Mumbai','maharastra','india');


insert into Location(id,landmark,city,state,country,pincode)
values
(117,'LA1','Mumbai','maharastra','india',NULL);


