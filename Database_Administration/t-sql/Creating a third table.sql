select Department as NumberOfDepartments
into tblDepartment2
from
(select Department, count(*) as NumberPerDepartments
from tblEmployee
GROUP BY Department) as newTable

select distinct Department, convert(varchar(20), N'') as DepartmentHead
into tblDepartment
from tblEmployee

drop table tblDepartment

alter table tblDepartment
alter column DepartmentHead varchar(30) null


