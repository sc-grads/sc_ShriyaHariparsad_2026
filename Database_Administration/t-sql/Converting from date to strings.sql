declare @mydate as datetime = '2015-06-25 01:02:03.456'
select 'The date and time is: ' + @mydate
go
declare @mydate as datetime = '2015-06-25 01:02:03.456'
select convert(nvarchar(20),@mydate) as MyConvertedDate
go
declare @mydate as datetime = '2015-06-25 01:02:03.456'
select cast(@mydate as nvarchar(20)) as MyCastDate

select convert(date,'Thursday, 25 June 2015') as MyConvertedDate
select parse('Thursday, 25 June 2015' as date) as MyParsedDate
select parse('Jueves, 25 de junio de 2015' as date USING 'es-ES') as MySpanishParsedDate

select format(cast('2015-06-25 01:02:03.456' as datetime),'D') as MyFormattedLongDate
select format(cast('2015-06-25 01:02:03.456' as datetime),'d') as MyFormattedShortDate
select format(cast('2015-06-25 01:02:03.456' as datetime),'dd-MM-yyyy') as MyFormattedBritishDate
select format(cast('2015-06-25 01:02:03.456' as datetime),'D','de-DE') as MyForamttedInternationalLongDate
