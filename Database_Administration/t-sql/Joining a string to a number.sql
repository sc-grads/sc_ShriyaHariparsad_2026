Select 'My Number is: ' + convert(varchar(20),4567)
Select 'My Number is: ' + cast(4567 as varchar(20))

select 'My salary is: $' + convert(varchar(20),2345.6) --works, but not well
select 'My salary is: ' + format(2345.6,'C','fr-FR')
