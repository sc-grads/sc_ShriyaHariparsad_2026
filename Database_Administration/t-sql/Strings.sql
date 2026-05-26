--char
--varchar
--nchar
--nvarchar

ASCII
UNICODE

DECLARE @chrMyCharacters as char(10)
set @chrMyCharacters = 'hellothere'
select @chrMyCharacters, len(@chrMyCharacters) as MyLength, DATALENGTH(@chrMyCharacters) as myDataLength

go

DECLARE @chrMyCharacters as varchar(10)
set @chrMyCharacters = 'hellothere'
select @chrMyCharacters, len(@chrMyCharacters) as MyLength, DATALENGTH(@chrMyCharacters) as myDataLength

go

DECLARE @chrMyCharacters as nvarchar(10)
set @chrMyCharacters = 'hello'
select @chrMyCharacters, len(@chrMyCharacters) as MyLength, DATALENGTH(@chrMyCharacters) as myDataLength
