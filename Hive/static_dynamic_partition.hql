Hive Tables
    Internal/Managed Tables
    External Tables

Internal/Managed Tables
    If I drop table ? - data also will gets dropped
    When I create table, what happens in HDFS ? 
        table structure gets stored in metastore
        an empty directory gets created in default hive warehouse directory
    When I load data using load data local inpath hive command
        data gets copied to respective HDFS directory of the hive table

Emp_ID,E_FName,E_LName,E_Mail,Gender,E_PHNO,E_Salary,E_DOB,E_DOJ,E_CITY,E_DEP
101,Mahesh,Dasari,Mahesh.Dasari@gmail.com,Male,7123456789,500,20-06-1998,10-06-2015,NKBD,DBA

create database practice;

CREATE TABLE practice.employee_data
(
    Emp_ID int,
    FName string,
    LName string ,
    Mail string ,
    Gender string,
    PHNO BIGINT,
    Salary INT,
    DOB string,
    DOJ string,
    CITY string,
    DEP string
)
row format delimited
fields terminated by ","
lines terminated by "\n";


load data local inpath '/root/employee_data.csv' into table practice.employee_data;

CREATE database adi;


CREATE EXTERNAL TABLE adi.employee_data
(
    Emp_ID int,
    FName string,
    LName string ,
    Mail string ,
    Gender string,
    PHNO BIGINT,
    Salary INT,
    DOB string,
    DOJ string,
    CITY string,
    DEP string
)
row format delimited
fields terminated by ","
lines terminated by "\n"
location '/data/use_case/adi/employee/';



CREATE TABLE practice.employee_data
(
    id int,
    name string,
    salary int,
    age tinyint,
    city string
)
row format delimited
fields terminated by ","
lines terminated by "\n";

load data local inpath '/root/new_data.csv' into table practice.employee_data;

CREATE TABLE practice.employee_data_part
(
    id int,
    name string,
    salary int,
    age tinyint
)
partitioned by (city string)
row format delimited
fields terminated by ","
lines terminated by "\n";


insert into table practice.employee_data_part partition(city = 'Bengaluru')
select id, name, salary, age from practice.employee_data where city = 'Bglr';

insert into table practice.employee_data_part partition(city = 'Hyderabad')
select id, name, salary, age from practice.employee_data where city = 'Hyd';


insert into table practice.employee_data_part partition(city = 'Chn')
select id, name, salary, age from practice.employee_data where city = 'Chn';



Dynmaic Partitioning

CREATE TABLE practice.employee_data_dyn_part
(
    id int,
    name string,
    salary int,
    age tinyint
)
partitioned by (city string)
row format delimited
fields terminated by ","
lines terminated by "\n";


set hive.exec.dynamic.partition.mode=nonstrict

insert into table practice.employee_data_dyn_part partition(city)
select id, name, salary, age, city from practice.employee_data;

