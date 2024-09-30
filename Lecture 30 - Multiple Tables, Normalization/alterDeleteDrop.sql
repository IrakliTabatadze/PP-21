

update customer1 set date_of_birth = '2023-08-20' where customerid = 2

select * from customer1 order by last_name

delete from customer1 where first_name = 'Irakli'

truncate customer


alter table customer1 add column salary1 integer
alter table customer1 alter column salary type float
alter table customer1 drop column salary

drop table customer
