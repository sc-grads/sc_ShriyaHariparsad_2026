create table salesstaff 
(
  staffid int not null primary key, 
  fName nvarchar(30) not null,
  lName nvarchar(30) not null
  )

insert into salesstaff (staffid,fName,lName) VALUES (200,'abbas','mehmood')

select * from salesstaff

insert into salesstaff (staffid,fName,lName) VALUES (300,'Imran','Afzal'),(325,'john','vick'),(314,'james','dino')

create table salesstaffNew
(
  ID INT NOT NULL IDENTITY PRIMARY KEY,
  staffid int not null,
  fName nvarchar(30),
  lName nvarchar(30) 
  )

  insert into salesstaffNew(staffid,fName,lName) VALUES (200,'abbas','mehmood')
  insert into salesstaffNew(staffid,fName,lName) VALUES (300,'Imran','Afzal'),(325,'john','vick'),(314,'james','dino')


  select * from salesstaffNew

  create table nameOnlyTable
(
  fName nvarchar(30),
  lName nvarchar(30) 
  )

  select * from nameOnlyTable

  insert nameOnlyTable (fName,lName)
  select fName,lName from salesstaffNew where id>= 3

  select * into salesstaffNew_bkp from salesstaffNew

  select * from salesstaffNew_bkp