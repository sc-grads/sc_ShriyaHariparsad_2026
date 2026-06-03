create clustered index idx_tblEmployee on [dbo].[tblEmployee]([EmployeeNumber])

drop index idx_tblEmployee on [dbo].[tblEmployee]

select * from [dbo].[tblEmployee2] where [EmployeeNumber] = 127
select * from [dbo].[tblEmployee2]

select *
into [dbo].[tblEmployee2]
from [dbo].[tblEmployee]
where EmployeeNumber <> 131

--seek = few number of rows based on the index
--scan = going through the entire table

alter table [dbo].[tblEmployee2]
add constraint pk_tblEmployee2 PRIMARY KEY(EmployeeNumber)

create table myTable (Field1 int primary key)
