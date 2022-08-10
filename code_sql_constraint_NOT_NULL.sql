mysql -u root -p

drop database db99;
show databases;
create database db99;
show databases;
use db99;

drop table Location;
create table Location
(
    id int,
    landmark varchar(20),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    pincode int
);
desc Location;
select * from Location;

insert into Location
values
(111,'LA1','Mumbai','maharastra','india',408303),
(112,'LA11','Palghar','maharastra','india',405303),
(113,'LA2','Pune','maharastra','india',401903),
(114,'LA3','Nagpur','maharastra','india',409303);

select * from Location;
