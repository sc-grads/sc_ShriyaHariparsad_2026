CREATE TRIGGER TR_tblTransaction
ON tblTransaction
AFTER DELETE, INSERT, UPDATE
AS
BEGIN
	select * from Inserted
	select * from Deleted
END
GO

