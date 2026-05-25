CREATE PROCEDURE SelectAllPersonAddress
AS
Select * FROM Person.Address
go;

select * from Person.Address

execute SelectAllPersonAddress

drop procedure SelectAllPersonAddress

CREATE PROCEDURE SelectAllPersonAddressWithParamwithEncryption (@city nvarchar(30) = 'New York')
WITH ENCRYPTION
AS
BEGIN
SET NOCOUNT ON

Select * FROM Person.Address where City = @city;
END

exec SelectAllPersonAddressWithParam @city = 'Miami'
exec SelectAllPersonAddressWithParam 'Miami'

