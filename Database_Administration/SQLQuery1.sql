CREATE TABLE [AdventureWorks2025].[sales].[visits] (
visit_ID INT PRIMARY KEY IDENTITY (1,1),
first_name VARCHAR (50) not null,
last_name VARCHAR (50) not null,
visited_at datetime,
phone VARCHAR (20) not null,
store_id INT not null,
FOREIGN KEY (store_id) REFERENCES sales.storeNEW (store_id)
)

CREATE TABLE [AdventureWorks2025].[sales].[storenew] (

store_id INT not null,
sales INT 
)
FOREIGN KEY (store_id) REFERENCES sales.storenew (store_id)
)

SELECT * FROM [AdventureWorks2025].[sales].[visits]

 select BusinessEntityID,firstname,lastname,Title
 into #TempPersonTable
 from Person.Person
 where title = 'mr.'


select BusinessEntityID,firstname,lastname,Title

 from Person.Person
 where title = 'mr.'

SELECT * FROM #TempPersonTable

DROP TABLE #TempPersonTable