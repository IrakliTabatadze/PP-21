-- მონაცემთა ბაზის შექმნა
create database databasename


-- ცხრილის შექმნა
create table customer1(customerid serial primary key not null,
last_name varchar(20),
first_name varchar(20),
date_of_birth date
)

-- ცხრილში ინფორმაციის ჩაწერა
insert into customer1 values(1, 'Doe', 'John', '2015-09-25')
insert into customer1(last_name, first_name, date_of_birth) values('Doe', 'John', '2010-08-10'),('Doe', 'John', '2010-08-10'),('Doe', 'John', '2010-08-10'),('Doe', 'John', '2010-08-10')


-- ცხრილიდან ინფორმაციის წაკითხვა
select * from customer1
select first_name, last_name from customer1
select * from customer1 where customerid = 2 or customerid = 5
select * from customer1 where customerid = 2 and first_name = 'john'
select * from customer1 where first_name like 'Ira%'
select * from customer1 where first_name like '%li'
select * from customer1 where first_name like '%h%'