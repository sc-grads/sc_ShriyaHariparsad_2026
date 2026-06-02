ALTER FUNCTION [dbo].[TransactionList](@EmployeeNumber int)
RETURNS TABLE AS RETURN
(
    SELECT * FROM tblTransaction
    WHERE EmployeeNumber = @EmployeeNumber
)
go
SELECT * 
from dbo.TransactionList(123)
GO
CREATE FUNCTION TransList(@EmployeeNumber int)
RETURNS @TransList TABLE
(Amount smallmoney,
DateOfTransaction smalldatetime,
EmployeeNumber int)
AS
BEGIN
    INSERT INTO @TransList(Amount, DateOfTransaction, EmployeeNumber)
    SELECT Amount, DateOfTransaction, EmployeeNumber FROM tblTransaction
    WHERE EmployeeNumber = @EmployeeNumber
    RETURN
END
