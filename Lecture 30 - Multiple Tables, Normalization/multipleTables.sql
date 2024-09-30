-- ცხრილების შექმნა

create table customers(
    customerid integer not null,
    lastname varchar(40) not null,
    firstname varchar(40) not null,
    dateofbirth date,
    cityid integer not null,
    zipcode varchar(4),
    street varchar(60),
    housenumber integer,
    income float
)



create table cities(
    cityid serial primary key,
    cityname varchar(30)
)


create table accounttypes(
    accounttypeid serial primary key,
    accounttypename varchar(50)
)


create table accounts(
    accountnumber varchar(100),
    customeridnumber integer,
    accounttypeid integer,
    balance float
)


-- სვეტზე უნიკალურობის დადება
alter table accounts add constraint uniqueaccountnumber unique (accountnumber)
alter table customers add constraint customeridunique unique (customerid)

-- გარე გასაღების დადება
alter table accounts add constraint accounttypefk foreign key (accounttypeid) references accounttypes(accounttypeid)
alter table accounts add constraint customeridfk foreign key (customeridnumber) references customers(customerid)

alter table customers add constraint cityidfk foreign key (cityid) references cities(cityid)


insert into cities(cityname) values ('Tbilisi'), ('Batumi'), ('Qutaisi'), ('Qobuleti')


insert into customers(customerid, lastname, firstname, cityid) values('1231233', 'Johnson', 'Kate', 4)


insert into accounttypes(accounttypename) values ('Visa'), ('MasterCard'), ('Amex')


insert into accounts values ('GE00BG00000012345678', '123123', 2, 1000.50), ('GE00BG00000012344444', '123123', 1, 100.50)