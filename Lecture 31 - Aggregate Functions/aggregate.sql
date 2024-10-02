select * from customers

-- Joins
select customerid, lastname, firstname, cityname from customers left join cities on customers.cityid = cities.cityid
select customerid, lastname, firstname, cityname from customers right join cities on customers.cityid = cities.cityid
select customerid, lastname, firstname, cityname from customers inner join cities on customers.cityid = cities.cityid
select customerid, lastname, firstname, cityname from customers full join cities on customers.cityid = cities.cityid


select customerid, lastname, firstname, cityname, accountnumber, accounttypename, balance from customers
    left join cities on customers.cityid = cities.cityid
    left join accounts on customers.customerid = accounts.customeridnumber
    left join accounttypes on accounts.accounttypeid = accounttypes.accounttypeid
group by customerid, lastname, firstname, cityname, accountnumber, accounttypename, balance


-- View
create view JoinView as
select customerid, lastname, firstname, cityname, accountnumber, accounttypename, balance from customers
    left join cities on customers.cityid = cities.cityid
    left join accounts on customers.customerid = accounts.customeridnumber
    left join accounttypes on accounts.accounttypeid = accounttypes.accounttypeid


select * from joinview


-- Agregate Functions
select sum(income) as jami from customers where cityid is not null
select avg(income) as average from customers
select min(income) from customers
select max(income) from customers

select count(*) from customers

select distinct(cityid) from customers


select cityid, sum(income), avg(income), max(income), min(income) from customers group by cityid having sum(income) > 75000



-- Triggers
alter table customers add column create_date timestamp


create or replace function set_create_date()
returns trigger as $$
    begin
        NEW.create_date = NOW();
        RETURN NEW;
    end;
    $$ language plpgsql;


create trigger set_create_date_trigger
before insert on customers
for each row
execute function set_create_date()


insert into customers(lastname, firstname, customerid) values('Doe', 'Kate', '15')

update customers set firstname = 'Irakl' where customerid = 15


alter table customers add column update_date timestamp

create or replace function set_update_date()
returns trigger as $$
    begin
        NEW.update_date = NOW();
        RETURN NEW;
    end;
    $$ language plpgsql;


create trigger set_update_date_trigger
before update on customers
for each row
execute function set_update_date()