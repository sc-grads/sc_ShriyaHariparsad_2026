-- Initialise a variable, give it a data type and an initial value

Declare @myvar AS numeric(7,2) = 3

SELECT POWER(@myvar,3)
SELECT SQUARE(@myvar)
SELECT POWER(@myvar,0.5)
SELECT SQRT(@myvar)

GO

Declare @myvar as numeric(7,2) = 12.345

SELECT FLOOR(@myvar) as myFloor
SELECT CEILING(@myvar) as myCeiling
SELECT ROUND(@myvar,2) as myRound

GO
