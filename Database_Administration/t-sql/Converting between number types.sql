--IMPLICIT

DECLARE @myvar as Decimal(5,2) = 3

SELECT @myvar

--explicit

SELECT CONVERT(decimal(5,2),3)/2
SELECT CAST(3 as decimal(5,2))/2

select convert(int,12.345)+convert(int,12.7)
select convert(int,12.345+12.7)