create nonclustered index idx_tblEmployee_DateOfBirth on [dbo].[tblEmployee]([DateOfBirth])
create nonclustered index idx_tblEmployee_DateOfBirth_Department on [dbo].[tblEmployee]([DateOfBirth],Department)

drop index idx_tblEmployee on [dbo].[tblEmployee]

select * from [dbo].[tblEmployee2] where [EmployeeNumber] = 127
select * from [dbo].[tblEmployee2]

select DateOfBirth, Department
from [dbo].[tblEmployee]
where DateOfBirth>='1992-01-01' and DateOfBirth<'1993-01-01'

--seek = few number of rows based on the index
--scan = going through the entire table

alter table [dbo].[tblDepartment]
add constraint unq_tblDepartment UNIQUE(Department)

