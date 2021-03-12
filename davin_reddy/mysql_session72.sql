show databases;

create database test_database;

use test_database;

create table student(name varchar(20),college varchar(20));

insert into student values ('a','a1'), ('b','b2');
select * from student;
