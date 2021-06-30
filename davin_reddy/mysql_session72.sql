show databases;

create database test_database;

use test_database;

create table student(name varchar(20),college varchar(20));

insert into student values ('a','a1'), ('b','b2');
select * from student;

ALTER TABLE student ADD image varbinary(max);
insert into student (image varbinary(max));
create table student2(image varbinary(max));

CREATE TABLE Employees
(
    Id int,
    Name varchar(50) not null,
    Photo varbinary(max) not null
)


INSERT INTO Employees (Id, Name, Photo) 
SELECT 10, 'John', BulkColumn 
FROM Openrowset( Bulk 'C:\photo.bmp', Single_Blob) as EmployeePicture
