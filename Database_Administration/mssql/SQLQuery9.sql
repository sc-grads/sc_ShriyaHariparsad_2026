select
FirstName +''+ LastName as FullName,
TerritoryName,
TerritoryGroup,
SalesQuota,
SalesYTD,
SalesLastYear
into SalesStaff
from 
sales.vSalesPerson

select * from [Sales].[vSalesPerson]

drop table SalesStaff

select * from SalesStaff

update SalesStaff SET salesquota = 50000.00
update SalesStaff SET salesquota = salesquota + 150000.00
update SalesStaff SET salesquota = salesquota + 150000.00,salesYTD=salesYTD-500,saleslastyear= saleslastyear *1.50

update SalesStaff SET territoryname = 'UK' where territoryname = 'United Kingdom'

update SalesStaff SET territoryname = 'UK',territorygroup = 'europe' where territorygroup is null and fullname = 'SyedAbbas'

update salesstaff set salesquota = sp.salesquota
from salesstaff ss
inner join sales.vSalesPerson sp
on ss.fullname = (sp.firstname +''+ sp.lastname)

