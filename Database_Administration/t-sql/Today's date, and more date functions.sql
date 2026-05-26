Select CURRENT_TIMESTAMP as RightNow --standard version of getting the date and time
select getdate() as RightNow
select SYSDATETIME() as RightNow --more exact answer
select dateadd(YEAR,1,'2015-01-02 03:04:05') as myYear --lets you add one to the year
select datepart(hour,'2015-01-02 03:04:05') as myHour --allows us to extract the hour
select datename(month,getdate()) as myAnswer --gets the month
select datediff(SECOND,'2015-01-02 03:04:05',getdate()) as SecondsElapsed 
