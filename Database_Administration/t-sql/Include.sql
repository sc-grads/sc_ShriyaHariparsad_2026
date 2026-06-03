CREATE NONCLUSTERED INDEX idx_tblEmployee_Employee  
    ON dbo.tblEmployee(EmployeeNumber) include (EmployeeFirstName);

DROP INDEX idx_tblEmployee_Employee ON dbo.tblEmployee


