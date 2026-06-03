select *
from [dbo].[tblEmployee] as E
left join [dbo].[tblDepartment] as D
on E.Department = D.Department


