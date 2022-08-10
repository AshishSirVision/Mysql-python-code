mysql -u root -p

drop database db99;
show databases;
create database db99;
show databases;
use db99;

drop table Location;
 drop table PINC;
 create table PINC
 (
     id int,
     pcode int primary key
 );
desc PINC;
select * from PINC;
insert into PINC
values
(1,401303),
(2,401307),
(5,401306),
(6,401305);
select * from PINC;



create table Location
(
    id int not null  AUTO_INCREMENT primary key,
    landmark varchar(20),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    pincode int,
    foreign key(pincode) references PINC(pcode)
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


insert into Location(landmark,city,state,country,pincode)
values
('LA1','Mumbai','maharastra','india',401303),
('LA11','Palghar','maharastra','india',401303),
('LA2','Pune','maharastra','india',401307),
('LA3','Nagpur','maharastra','india',401306);

select * from Location;
