show databases;

create database test_database;

use test_database;

create table student(name varchar(20),college varchar(20));

insert into student values ('a','a123'), ('b','b1233');
select * from student;
