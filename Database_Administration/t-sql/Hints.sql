select D.Department, D.DepartmentHead, E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName 
from [dbo].[tblDepartment] as D  WITH (NOLOCK)
left join [dbo].[tblEmployee] as E
on D.Department = E.Department
where D.Department = 'HR'

select D.Department, D.DepartmentHead, E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName 
from [dbo].[tblDepartment] as D  WITH (REPEATABLEREAD)
left join [dbo].[tblEmployee] as E
on D.Department = E.Department
where D.Department = 'HR'
