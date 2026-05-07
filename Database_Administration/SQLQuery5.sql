/* Employee Table
[EmpID] [int] NOT NULL,
	[EmpName] [nvarchar](50) NULL,
	[EmpTitle] [nvarchar](50) NULL,


Sales Table

[EmpID] [int] NULL,
	[EmpName] [nvarchar](50) NULL,
	[SalesNumber] [int] NOT NULL,
	[ItemSold] [int] NULL,

	*/

select * from [dbo].[Employee]
select * from [dbo].[Sales]

select * from [dbo].[Employee] e
join [dbo].[Sales] s
on e.empid = s.empid

select e.EmpId,e.EmpName,s.SalesNumber,s.ItemSold from [dbo].[Employee] e
join [dbo].[Sales] s
on e.empid = s.empid
order by e.empid

SELECT count(s.SalesNumber),e.EmpID,e.EmpName FROM [dbo].[Employee] e
join [dbo].[Sales] s 
on e.EmpID = s.[EmpID]
group by e.EmpID,e.EmpName



