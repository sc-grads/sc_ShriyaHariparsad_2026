select tblEmployee.EmployeeNumber, EmployeeFirstName, EmployeeLastName, sum(Amount) as SumOfAmount
from tblEmployee
join tblTransaction
on tblEmployee.EmployeeNumber = tblTransaction.EmployeeNumber
GROUP BY tblEmployee.EmployeeNumber, EmployeeFirstName, EmployeeLastName
ORDER BY EmployeeNumber

select * from tblEmployee where EmployeeNumber = 1046

select * from tblTransaction where EmployeeNumber = 1046