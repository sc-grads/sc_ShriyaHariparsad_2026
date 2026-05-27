begin transaction

select count(*) from tblTransaction

delete tblTransaction
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber

where E.EmployeeNumber is null

select count(*) from tblTransaction

rollback transaction

select count(*) from tblTransaction
