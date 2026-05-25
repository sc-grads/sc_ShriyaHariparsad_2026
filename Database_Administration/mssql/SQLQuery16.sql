CREATE TABLE FunctionEmployee
(
EmpID int Primary key,
FirstName varchar(50) null,
LastName varchar(50) null,
Salary int null,
Address varchar(100) null,
)

insert into [FunctionEmployee] ([EmpID],[FirstName],[LastName],[Salary],[Address]) values (1,'Mohan','Chauahan', 22000, 'Delhi')
insert into [FunctionEmployee] ([EmpID],[FirstName],[LastName],[Salary],[Address]) values (2,'Asif','Khan', 15000, 'Delhi')
insert into [FunctionEmployee] ([EmpID],[FirstName],[LastName],[Salary],[Address]) values (3,'Bhuvnesh','Shakya', 19000, 'Noida')
insert into [FunctionEmployee] ([EmpID],[FirstName],[LastName],[Salary],[Address]) values (4,'Deepak','Kuman', 19000, 'Noida')

select * from FunctionEmployee

Create function fnGetEmpFullName
(@FirstName varchar(50), @LastName varchar(50))
returns varchar(101)
As
Begin
return (select @FirstName + ' ' +@LastName);
end 

select dbo.fnGetEmpFullName (FirstName, LastName) as FullName , Salary from FunctionEmployee

create function fnGetEmployee()
returns Table
As
return (select * from FunctionEmployee)

select * from dbo.FunctionEmployee

create function fnGetMulEmployee()
returns @Emp Table
(
Empid int,
FirstName varchar(50),
Salary int
)
As
Begin
Insert into @Emp Select e.EmpID,e.FirstName,e.Salary from FunctionEmployee e;
--Now update salary of first employee
 update @Emp set Salary=25000 where EmpID=1;
--It will update only in @Emp table not in Original Employee table
return
end 

select * from dbo.fnGetMulEmployee()