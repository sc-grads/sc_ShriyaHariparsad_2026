ALTER TRIGGER TR_tblTransaction
ON tblTransaction
AFTER DELETE, INSERT, UPDATE
AS
BEGIN
	--IF @@ROWCOUNT > 0
	BEGIN
		select * from Inserted
		select * from Deleted
	END
END
GO

update tblTransaction
set DateofTransaction = '2015-07-12'
where Amount = 123 and DateofTransaction = '2015-07-11' and EmployeeNumber = 123

insert into tblTransaction(Amount, DateOfTransaction, EmployeeNumber)
VALUES (123,'2015-07-11', 123)

SELECT * FROM ViewByDepartment where TotalAmount = -2.77 and EmployeeNumber = 132

begin tran
delete from ViewByDepartment
where TotalAmount = -2.77 and EmployeeNumber = 132
rollback tran

