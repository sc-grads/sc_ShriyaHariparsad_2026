DECLARE @chrASCII as varchar(10) = ' hello '

DECLARE @chrUNICODE as nvarchar(10) = N'hello'

select left(@chrASCII,2) as myASCII, right(@chrUNICODE,2) as myUNICODE
select substring(@chrASCII,3,2) as middleletters
select ltrim(rtrim(@chrASCII)) as TRIM
select replace (@chrASCII,'l','L')
select upper(@chrASCII) as myUpper
select lower(@chrASCII) as myLower
